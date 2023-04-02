Description

This code is a Python script that uses the Selenium library to scrape data from a website. Specifically, the website is the Health Facility Registry (HFR) for Nigeria, and the script scrapes information about hospitals from the registry.

The script first imports the necessary libraries, including Selenium and time. It then opens a web browser using the chrome  webdriver and navigates to the first page of the HFR website.

The script then enters a for loop that iterates through all the pages on the website (there are 20 pages in total). Within the for loop, there is a nested for loop that iterates through all the view buttons on the current page and gets the records contained in each view button using the .get_attribute method on the webdriver.

The data is stored in variables, and then written to a CSV file using the Python built-in "open" function. The "a" argument in the "open" function specifies that the file should be opened in append mode, so that data can be added to it. The "newline=''" argument is used to specify that the file should use the default line ending for the system.

Each record is written to the CSV file as a single line, with each field separated by a semicolon (;).

Finally, the script closes the browser and the CSV file.



Technologies Used
List the programming languages, libraries, and tools that you used in your project.
