from django.shortcuts import render
####################################
import datetime # FOR FINDING UTC TIME
####################################
####################################
# FOR SCRAPING WIKI ##################
import urllib, urllib2
import lxml.etree
import wikipedia
import scraperwiki
from bs4 import BeautifulSoup
from utils import *
import requests
from lxml import html
import json 





def findUTC():
    H= datetime.datetime.utcnow().strftime("%H")
    intH= int(H)
    current = (intH-17)*-1
    return current
   
 
  #url= "/https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
#     url = "https://en.wikipedia.org/wiki/List_of_ship_names_of_the_Royal_Navy_(A)"
#     wiki_html= urllib.urlopen(url)
#     soup = BeautifulSoup(wiki_html,"lxml")
    
 
   
def john():
    url= "https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
    r = requests.get(url)
    # r = urllib.urlopen(url)
    soup= BeautifulSoup(r.content,"lxml")
    # soup= BeautifulSoup(r,"lxml")

    links = soup.find_all("a")
    # for link in links:
    #     print link.text

    g_data = soup.find_all("span", {"id": "UTC.E2.88.9211:00.2C_X"})
    print g_data
john()

def amelia():
    currentUTC= str(findUTC())
    print currentUTC
    htmltext= urllib.urlopen("https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json")
    #https://raw.githubusercontent.com/moment/moment-timezone/develop/data/meta/latest.json
    data = json.load(htmltext)
    targetlist = []
    for zones in xrange(len(data)):
        utcs= data[zones]['text']
       # print str(utcs)
        wow= str(utcs)[5:7]
        
        if wow == currentUTC:
            print "these are the places:", utcs
            targetlist.append(utcs)
   # print targetlist
    return targetlist
            


# Create your views here.
def home(request):
    template= "home.html"
    now = datetime.datetime.now()
    test = str(now)
    realtime= test[11:]
    #print scrapewiki()
  #  print findUTC()
  
    newamelia=amelia()
    
    
    
    
    context={
        "now": now,
        "amelia":newamelia,
    }
    return render(request,template,context) 