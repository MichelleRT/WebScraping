"""

Webscrape from web pages. 

"""

from bs4 import BeautifulSoup
import re
import urllib2
import urllib

X_file = "http://www.enggcyclopedia.com/2011/01/octane-number/" 
page = urllib2.urlopen(X_file) 
soup = BeautifulSoup(page, "html.parser") 

for data in soup.find_all('tr')   