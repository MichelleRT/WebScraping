"""

Webscrape from web pages. 

"""

from bs4 import BeautifulSoup
import re
import urllib2
import io 

X_file = "http://www.enggcyclopedia.com/2011/01/octane-number/" 
page = urllib2.urlopen(X_file) 
soup = BeautifulSoup(page, "html.parser") 

# Open a new file for storing all the data 
fileout = io.open("EnggCycData.txt", encoding='utf-8', mode='a') 

for tags in soup.find_all('tr'):
    data = tags.text.strip()    # strip the tags away 
    fileout.write(data + "\n")    

# Close the file
fileout.close() 