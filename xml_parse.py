"""

Was having issues pulling data from the local file.
The code works just fine for websites.
Trying to fix these issues. 

"""

from bs4 import BeautifulSoup
import re
import urllib2
import urllib

# X_file = "file:///Users/mtse/Documents/metacyc_data/metabolic-reactions.xml"
# page = urllib2.urlopen(X_file).read() 
# page = urllib.urlopen("file:/Users/mtse/Documents/metacyc_data/metabolic-reactions.xml") 
page = open("/Users/mtse/Documents/metacyc_data/metabolic-reactions.xml")
soup = BeautifulSoup(page.read(), "html.parser")

print("working")