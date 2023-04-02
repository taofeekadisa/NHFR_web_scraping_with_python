import pandas as pd

#list containing the column names to be used in our dataframe
column = ["Id", "Facility_Code", "Registration_No", "Start_Date", "Facility_Name", "Alt_Facility_Name", "State",\
     "LGA", "Ward", "Ownership", "Ownership_Type", "Facility_Level", "Facility_Level_Option", "Physical_Location",\
     "Alternate_Number", "Longitude", "Latitude", "Postal_address", "Phone_Number", "Email_Address", "Website", "Operational_Days",\
     "Operation_Hour", "Operation_Status", "Registration_Status", "License_Status", "No_Of_Doctors", "No_Of_Pharmacists", "Dentist",\
     "Pharmacy_Technicians", "No_Of_Nurses", "No_Of_Lab_Scientists", "Midwifes", "Lab_Technicians", "Nurse_Midwife", "HIM_Officers",\
     "Community_Health_Officer", "Community_Extension_Workers", "Jun_Community_Extension_Worker", "Dental_Technicians", "Env_Health_Officers",\
    "Inpatient", "Outpatient", "No_Of_Beds", "Onsite_Laboratory", "Onsite_Imaging", "Onsite_Pharmarcy",\
     "Mortuary_Services", "No__Of_Attendants", "Ambulance_Services",  "State_Unique_Id"]

# Let's assume we have a CSV file named "test_hfr.csv" in the current directory
# We can read the CSV file using pandas read_csv function
df = pd.read_csv("raw_hfr.csv", delimiter = "|", header=None, names=column)

def remove_space(x):
    x = str(x)
    x = x.strip()
    return x


#remove leading and ending empty spaces in our all records and columns except Id which is an Int
for i in column:
    df[i] = df[i].apply(remove_space)

#list of selected columns to be made int
num_cols = ['No_Of_Doctors','No_Of_Pharmacists','Dentist','Pharmacy_Technicians','No_Of_Nurses',\
           'No_Of_Lab_Scientists','Midwifes','Lab_Technicians','Nurse_Midwife','HIM_Officers','Community_Health_Officer',\
  'Community_Extension_Workers','Jun_Community_Extension_Worker','Dental_Technicians','Env_Health_Officers','No_Of_Attendants']

#change the dtype of select few columns to Int64
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce').astype('Int64')

# Adamawa Bauchi Borno Gombe Taraba Yobe  North-East region.
# Zamfara Sokoto Kebbi Katsina Kano Kaduna Jigawa  North-west
# Plateau Niger Nasarawa Kwara Kogi Federal Capital Territory Benue  North-Central
# Imo Enugu Ebonyi Anambra Abia  South-East
# Rivers Edo Delta Cross River Bayelsa Akwa Ibom South-South
# Oyo Osun Ondo Ogun Lagos Ekiti South-West
north_east = ['Adamawa','Bauchi','Borno','Gombe','Taraba','Yobe']
north_west = ['Zamfara','Sokoto','Kebbi','Katsina','Kano','Kaduna','Jigawa']
north_cen = ['Plateau','Niger','Nasarawa','Kwara','Kogi','FCT','Benue']
south_east = ['Imo','Enugu','Ebonyi','Anambra','Abia']
south_south = ['Rivers','Edo','Delta','Cross River','Bayelsa','Akwa-Ibom']
south_west = ['Oyo','Osun','Ondo','Ogun','Lagos','Ekiti']

def get_zones(x):
    if x in north_east:
        return 'North-East'
    elif x in north_west:
        return 'North-West'
    elif x in north_cen:
        return 'North-Central'
    elif x in south_east:
        return 'South-East'
    elif x in south_south:
        return 'South-South'
    elif x in south_west:
        return 'South-West'
    else:
        return x
    
#create a column called Region that contains the geo-political zones of each state
df['Region'] = df['State'].apply(get_zones)

def get_year(x):
    x = x.split("-")
    x = x[0]
    return x

#get the year from the Start_Date column
df['Start_Year'] = df['Start_Date'].apply(get_year)

#change the dtype of the Start_Year to numeric and make it Int64 as it contains NA or non-int in it
df['Start_Year'] = pd.to_numeric(df['Start_Year'], errors='coerce').astype('Int64')

#change the dtype of start_date to datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce', infer_datetime_format=True)

#get the month from the Start_Date column
df['Start_Month'] = df['Start_Date'].dt.month

#change the start_date to date format
df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce', infer_datetime_format=True).dt.date

#change the dtype of start_month to int
new_df['Start_Month'].astype('Int64')

def clean_long(x):
    return x.replace(',', '0')

#clean the Longitude column
df['Longitude'] = df['Longitude'].apply(clean_long)


def clean_lat(x):
    x = str(x)
    
    if ':' in x:
        return x.replace(':','')
    elif '`' in x:
        return x.replace('`','')
    elif '+D' in x:
        return x.replace('+D','')
    elif '-' in  x:
        return x.replace('-','')
    else:
        return x

#clean the Latitude column
df['Latitude'] = df['Latitude'].apply(clean_lat)  

#create a column called Tenure that gets the tenure in year
df['tenure'] = df['Start_Year'].apply(lambda x: 2023 - x)

#create a new column containing the sum of all the health personnels

df['No_Of_Health_Personnel'] = df[['No_Of_Doctors','No_Of_Pharmacists','Dentist',\
        'Pharmacy_Technicians','No_Of_Nurses','No_Of_Lab_Scientists',\
        'Midwifes','Lab_Technicians','Nurse_Midwife','HIM_Officers',\
       'Community_Health_Officer','Community_Extension_Workers','Jun_Community_Extension_Worker',\
       'Dental_Technicians','Env_Health_Officers','No_Of_Attendants']].sum(axis=1)
#change the column names to lower case
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

df.to_csv("cleaned_hfr.csv")