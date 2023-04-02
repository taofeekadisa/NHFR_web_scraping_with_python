#import all neccessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv


serve = Service("/home/krissemmy/anaconda3/chromedriver_linux64/chromedriver.exe")
driver = webdriver.Chrome(service = serve)

#website url
website = 'https://hfr.health.gov.ng/facilities/hospitals-search?_token=zspcRufdE0S3URc5lbMKCGlf3knvrEMVf3jBUQO6&state_id=1&lga_id=&ward_id=&facility_level_id=0&ownership_id=0&operational_status_id=0&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0&service_category_id=0&facility_name=&entries_per_page=20'

#opening the website
driver.get(website)
driver.maximize_window()

# change from the default 20 entries per page to 500 page
select = driver.find_element(By.XPATH,'//*[@id="entries_per_page"]/option[7]')
select.click()

search = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/form/div[5]/div[3]/div/div[2]/button')
search.click()
time.sleep(3)

#code to scrape all the current records available on the website
#A for loop to iterate through all the pages on the website

for p in range(1,85,1):
    #opening a csv file in append mode, to add data into it with open('hospital_data.csv', 'a', newline='') as file:
    with open('raw_hfr.csv','a',newline='') as file:       
        
        #A nested for loop to iterate through all the view button, 
        #and get the records contained in each view buttton using the .get_attribute method on webdriver, on the current page
        for i in range(1,501):
            view_b = driver.find_element(By.XPATH, f'//*[@id="hosp"]/tbody/tr[{i}]/td[9]/a/button')
            time.sleep(4)
            view_b.click()
            time.sleep(4)
            #storing the data in variables
            ID = view_b.get_attribute('data-id')
            unique_id = view_b.get_attribute('data-unique_id')
            reg_no =  view_b.get_attribute('data-registration_no')
            start_date =  view_b.get_attribute('data-start_date')
            name =  view_b.get_attribute('data-facility_name')
            alt_name =  view_b.get_attribute('data-alt_facility_name')
            state =  view_b.get_attribute('data-state')
            lga =  view_b.get_attribute('data-lga')
            ward =  view_b.get_attribute('data-ward')
            ownership =  view_b.get_attribute('data-ownership')
            ownership_type =  view_b.get_attribute('data-ownership_type')
            level =  view_b.get_attribute('data-facility_level')
            level_option =  view_b.get_attribute('data-facility_level_option')
            phy_location =  view_b.get_attribute('data-physical_location')
            alt_nuber =  view_b.get_attribute('data-alternate_number')
            longitude =  view_b.get_attribute('data-longitude')
            latitude =  view_b.get_attribute('data-latitude')
            postal_address = view_b.get_attribute('data-postal_address')
            phone_num =  view_b.get_attribute('data-phone_number')
            email =  view_b.get_attribute('data-email_address')
            website =  view_b.get_attribute('data-website')
            operational_days =  view_b.get_attribute('data-operational_days')
            operational_hours =  view_b.get_attribute('data-operational_hours')
            operation_status =  view_b.get_attribute('data-operation_status')
            reg_status =  view_b.get_attribute('data-registration_status')
            license_status =  view_b.get_attribute('data-license_status')
            no_of_doctor =  view_b.get_attribute('data-doctors')
            no_of_pharmacist =  view_b.get_attribute('data-pharmacists')
            no_of_dentist =  view_b.get_attribute('data-dentist')
            no_of_pharmacy_technician =  view_b.get_attribute('data-pharmacy_technicians')
            no_of_nurse =  view_b.get_attribute('data-nurses')
            no_of_lab_scientist =  view_b.get_attribute('data-lab_scientists')
            no_of_midwife =  view_b.get_attribute('data-midwifes')
            no_of_lab_technician =  view_b.get_attribute('data-lab_technicians')
            no_of_nurse_midwife =  view_b.get_attribute('data-nurse_midwife')
            no_of_him_officer =  view_b.get_attribute('data-him_officers')
            no_of_comm_HO =  view_b.get_attribute('data-community_health_officer')
            no_of_comm_ext_worker =  view_b.get_attribute('data-community_extension_workers')
            no_of_jun_comm_ext_worker =  view_b.get_attribute('data-jun_community_extension_worker')
            no_of_dental_technician =  view_b.get_attribute('data-dental_technicians')
            no_of_env_HO =  view_b.get_attribute('data-env_health_officers')
            inpatient =  view_b.get_attribute('data-inpatient')
            outpatient =  view_b.get_attribute('data-outpatient')
            no_of_bed =  view_b.get_attribute('data-beds')
            onsite_lab =  view_b.get_attribute('data-onsite_laboratory')
            onsite_imaging =  view_b.get_attribute('data-onsite_imaging')
            onsite_phar =  view_b.get_attribute('data-onsite_pharmarcy')
            mortuary_service =  view_b.get_attribute('data-mortuary_services')
            no_of_attendant =  view_b.get_attribute('data-attendants')
            ambulance_service =  view_b.get_attribute('data-ambulance_services')
            state_unique_id =  view_b.get_attribute('data-state_unique_id')
            #writing all the data collected into a csv file aliased as 'file'
            file.write(f"{ID}| {unique_id}| {reg_no}| {start_date}| {name}| {alt_name}| {state}| {lga}| {ward}| {ownership}| {ownership_type}| {level}| {level_option}| {phy_location}| {alt_nuber}| {longitude}| {latitude}| {postal_address}| {phone_num}| {email}| {website}| {operational_days}| {operational_hours}| {operation_status}| {reg_status}| {license_status}| {no_of_doctor}| {no_of_pharmacist}| {no_of_dentist}| {no_of_pharmacy_technician}| {no_of_nurse}| {no_of_lab_scientist}| {no_of_midwife}| {no_of_lab_technician}| {no_of_nurse_midwife}| {no_of_him_officer}| {no_of_comm_HO}| {no_of_comm_ext_worker}| {no_of_jun_comm_ext_worker}| {no_of_dental_technician}| {no_of_env_HO}| {inpatient}| {outpatient}| {no_of_bed}| {onsite_lab}| {onsite_imaging}| {onsite_phar}| {mortuary_service}| {no_of_attendant}| {ambulance_service}| {state_unique_id}\n")
            time.sleep(4)

            close_button = driver.find_element(By.XPATH, '//*[@id="view_details"]/div/div/div[2]/div[2]/button')
            close_button.click()
            time.sleep(4)
    next_p = driver.find_element(By.LINK_TEXT,'›')
    next_p.click()
    time.sleep(5)

#close the driver
driver.close()