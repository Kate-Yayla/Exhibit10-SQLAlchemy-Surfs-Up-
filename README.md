# Surfs Up!


### Overview

* I have done the climate analysis for a trip to Honolulu, Hawaii!

![surfs-up.png](Images/surfs-up.png)

## Climate Analysis

I have used Python, SQLAlchemy and Matplotlib for the data exploration of climate database for the following steps:

* created engine to retrieve the data from hawaii.sqlite file,
* choosed a start date and end date for my analysis,
* found out the most active stations,
* calculated the lowest, highest, and average temperature for the station 'USC00519281',
* plotted the temperature observation. 

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data,
* Selected only the `date` and `prcp` values,
* Loaded the query results into a Pandas DataFrame and set the index
* Sorted the DataFrame values by `date`,
* Plotted the results using the DataFrame `plot` method.

 
  ![precipitation](Images/precipitation.png)

  ##### Used Pandas to calculate the summary statistics for the precipitation data.

   ![precipitation](Images/describe.png)

### Station Analysis

* Designed a query to calculate the total number of stations. There are 9 stations available to get a data. 
* Designed a query to find the most active stations.
  * Listed the stations and temperature observation counts in descending order.
* Designed a query to retrieve the last 12 months of temperature observation data (tobs).
  * Filtered by the station with the highest number of observations (about 80 Celcius)
  * Plotted the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

Designed Flask API based on the queries.

### API Routes

* `/`

  * Welcome home page.
  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Returned the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Returned a JSON list of temperature observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

### Temperature Analysis I

* Used hawaii_measurements.csv file for data,
* Used pandas read_csv,
* Found the average temperature in June and December for all stations as well as the years in the dataset,
* Run the unpaired t-test using independent in code as we have independent datasets (June and December) and p value determines whether the difference in the mean if there is statistical mean. There is only 3.9 degrees Celsius, and the mean temperatures in June and December in all stations between 2010-2017. Unpaired T-test conducted, p-value is very low than standard threshold, so null hypothesis is rejected. The difference between June and December could be considered as statistically signaficant. 

### Temperature Analysis II

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year,

* Plotted the min, avg, and max temperature from your previous query as a bar chart,
  * Used the average temperature as the bar height,
  * Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR),

###### Here is the bar chart created based given data. 

  ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates, analyzed for a week data,
* Calculated the daily normals,
* Created a list of dates for my trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and appended the results to a list,
* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date,
* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)


