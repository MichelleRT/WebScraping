"""

The point of this program is to web scrape data into text files for training features/weights 
in BioCompoundML. However, right now, we are keeping the web scraping and training separate, 
hence we are keeping the web scraping and training programs in different repositories.

Since no other sufficient databases for fuels containing the fuel properties RON (research 
octane number), TSI (threshold soot index), and MP (melting point) can be found, we are only 
taking data from the fuel engine co-op database 
(url: https://fuelsdb.nrel.gov/fmi/webd/FuelEngineCoOptimization).   

However, in order to make sure we can still pull data from other websites, this program can 
be used to pull data from any website. 

Reference: http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup 

"""
import requests
from bs4 import BeautifulSoup

# Get the fuel engine co-op database url
fuel_url = raw_input("Enter a website URL to extract data from: ") 
fuel_data = requests.get(fuel_url) 

# We want the fuel properties data in a text file
fuel_properties_data = fuel_data.text 
soup_data = BeautifulSoup(fuel_properties_data) 
for link in soup_data.find_all('RON'): 
  print(link.get('href') 



