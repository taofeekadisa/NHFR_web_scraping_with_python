
NHFR WEB SCRAPING PROJECT WITH PYTHON

This Python script uses the Selenium library to scrape data from the Health Facility Registry (HFR) for Nigeria. It collects information about hospitals from the registry, and saves the data to a CSV file. The script utilizes the Chrome web driver and a for loop to navigate through all 20 pages of the HFR website, and collects records from each page using a nested for loop. The data is then written to a CSV file using the built-in "open" function, and stored as a single line with each field separated by a semicolon.

Technologies Used:

•	Programming languages: Python

•	Libraries: selenium, time, csv, sqlalchemy, and Pandas

•	PostgreSQL

Cleaning and Pre-processing with Pandas: 


The script uses Pandas to clean and pre-process the data. The following steps were taken:


1.	The dataset is loaded from a CSV file using pandas.read_csv().
2.	Rows with missing data are removed using pandas.dropna().
3.	Duplicate rows are removed using pandas.drop_duplicates().
4.	Rows with invalid or inconsistent data are removed using pandas.query().
5.	The date column is converted to a datetime object using pandas.to_datetime()

Output:

The web_scraping_NHFR script now contains cleaned data. The CSV file contains the same columns as the original dataset, but with any missing or inconsistent data removed, and the date column converted to a datetime object.

Loading Pandas DataFrames to PostgreSQL using SQLAlchemy:


The script provides an example of how to load data from a Pandas DataFrame to a PostgreSQL database using SQLAlchemy. To use this functionality, prepare your data as a Pandas DataFrame, and import the load_to_postgresql function from pandas_to_postgresql.py. Then, call the function with the DataFrame as the first argument.

Loading Pandas to Postgres using sqlalchemy:


The script provides an example of how to load data from a Pandas DataFrame to a PostgreSQL database using SQLAlchemy. To use this functionality, prepare your data as a Pandas DataFrame, and import the load_to_postgresql function from pandas_to_postgresql.py. Then, call the function with the DataFrame as the first argument.

Data Analysis Using PostgreSQL


<a href=" NHFR_web_scraping_with_python/NHFR_query.sql at main · taofeekadisa/NHFR_web_scraping_with_python (github.com) ">Data Analysis SQL Query</a>
