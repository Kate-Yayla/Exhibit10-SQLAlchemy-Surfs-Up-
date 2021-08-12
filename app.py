import sqlalchemy
import numpy    as np
import pandas   as pd
import datetime as dt
from   sqlalchemy.orm         import Session
from   sqlalchemy.ext.automap import automap_base
from   sqlalchemy import create_engine, func, inspect
from   flask      import Flask, jsonify
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base   = automap_base()
Base.prepare(engine, reflect=True)
Tables      = Base.classes.keys()
Measurement = Base.classes.measurement
Station     = Base.classes.station
# Flask Setup
#################################################

app = Flask(__name__)


# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the list of available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&ltstart&gt<br/>" f"Please Don't Forget to Use Date Format YYYY-MM-DD.<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt<br/>" f"Please Don't Forget to Use Date Format YYYY-MM-DD."    
    )
#################################################


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    """Return a list of precipitation values"""
    # Query
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    # Create a dictionary and fill up to a list of all precipitation
    all_precipitation = []
    for date, precipitation in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = precipitation
        all_precipitation.append(precipitation_dict)
    return jsonify(all_precipitation)
#################################################


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """Return a list of stations"""
    # Query 
    results = session.query(func.distinct(Measurement.station)).all()
    session.close()
    all_stations = list(np.ravel(results))
    return jsonify(stations=all_stations)
#################################################


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    """Return a list of dates and temps for the most active station"""
    # Query
    EndDate   = dt.datetime.strptime(session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0], '%Y-%m-%d')
    QueryDate = dt.datetime.strftime((EndDate - dt.timedelta(365)), '%Y-%m-%d')
    results   = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= QueryDate).\
    filter(Measurement.station == "USC00519281").\
    order_by(Measurement.date).all()
    session.close()
    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))
    return jsonify(all_tobs)
#################################################


@app.route("/api/v1.0/<start_date>")
def tobs_2(start_date):
    session = Session(engine)
        # Parse start date into datetime    
    # Query
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.station == "USC00519281").all()
    session.close()
    tobs_summary = {}
    tobs_summary["TMIN"] = results[0][0]
    tobs_summary["TAVG"] = results[0][1]
    tobs_summary["TMAX"] = results[0][2]
    return jsonify(tobs_summary)
#################################################


@app.route("/api/v1.0/<start_date>/<end_date>")
def tobs_3(start_date, end_date):
    session = Session(engine)
    # Query
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.date <= end_date).\
    filter(Measurement.station == "USC00519281").all()
    session.close()
    tobs_summary = {}
    tobs_summary["TMIN"] = results[0][0]
    tobs_summary["TAVG"] = results[0][1]
    tobs_summary["TMAX"] = results[0][2]
    return jsonify(tobs_summary)

if __name__ == '__main__':
    app.run(debug=True)