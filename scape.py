"""

The point of this program is to web scrape data into text files for training features/weights 
in BioCompoundML. However, right now, we are keeping the web scraping and training separate, 
hence we are keeping the web scraping and training programs in different repositories.

Since no other sufficient databases for fuels containing the fuel properties RON (research 
octane number), TSI (threshold soot index), and MP (melting point) can be found, we are only 
taking data from the fuel engine co-op database 
(url: https://fuelsdb.nrel.gov/fmi/webd/FuelEngineCoOptimization).   

"""
# import requests # so we can still web scrape even with page timeouts
# from bs4 import BeautifulSoup
# import urllib2

# """
# For timeout handling, I referenced this website:
# http://winstonlarson.com/scraping-timeouts 

# """
# timeout = 60 
# url = https://fuelsdb.nrel.gov/fmi/webd/FuelEngineCoOptimization

# while True: 
#   try: 
#     webpage = requests.get(url, timeout=60)
#     page = urllib2.urlopen(webpage)
#     soup = BeautifulSoup(page, "html.parser")
#     print("This is the soup html: ", soup)
#     break
#   except requests.exceptions.RequestException as e: # If doesn't work, then try again
#     pass

# webpage = "https://fuelsdb.nrel.gov/fmi/webd/FuelEngineCoOptimization"
# page = urllib2.urlopen(webpage) # This will get the HTML page of the url

# # find the data we want!
# soup = BeautifulSoup(page, "html.parser") # HTML parsing 
# print("This is the soup html: ", soup) # to see what we are actually getting 

# # the session keeps expiring...
# # so now I've just exported the file for now 



"Section for parsing a .xml file (should be similar to parsing HTML)"
from bs4 import BeautifulSoup
import urllib 
# import re

file = urllib.urlopen("file:/Users/mtse/Documents/metacyc_data/metabolic-reactions.xml") 
soup = BeautifulSoup(file, "html.parser") 
# print(soup)
print('a')

# for compartment_tag in soup.find_all("compartment"):
#     print compartment_tag.text, compartment_tag.next_sibling


