import pandas as pd
from sqlalchemy import create_engine

#LOADING THE DATAFRAME TO POSTGRESQL
df = pd.read_csv("cleaned_hfr.csv") #, delimiter = "|", header=None, names=column)

#Accepts user inputs for the database connection 
user = input("input your database username: ")
db_name = input("input your database name: ")
password = input("input your database password: ")
host = input("input your connection url/hostname: ")
port = input("input your connection port: ")

#create an engine variable to initiate connection to the postgres database
engine = create_engine(f'postgresql://{user}:{str(password)}@{str(host)}:{str(port)}/{str(db_name)}')

#load the dataframe into the database
df.to_sql('health_facility_registry', engine,index=False, if_exists='replace')

print(f"table {file_name} imported to db completed")
