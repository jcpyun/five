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


def amelia():
    htmltext= urllib.urlopen("https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json")
    data = json.load(htmltext)
    
    for zones in xrange(len(data)):
        print data[zones]['text']
    
amelia()
# def apitest(): 
#     #http://2015.compjour.org/tutorials/exploring-wikipedia-api-via-python/
#     # resp = requests.get("http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=Hello")
#     # print resp.status_code   #  200
#     # print resp.json() 
#     base_url="http://en.wikipedia.org/w/api.php"
#     UTCs=["UTC%E2%88%9212:00,"]
    
#     # https://en.wikipedia.org/wiki/UTC%E2%88%9212:00
    
# apitest()

# def my():
#     baseurl = 'http://en.wikipedia.org/w/api.php'
#     schools = ['Brown University',
#     'Columbia University',
#     'Cornell University',
#     'Dartmouth College',
#     'Harvard University',
#     'University of Pennsylvania',
#     'Princeton University',
#     'Yale University',
#     'Stanford University']


#     my_atts = {'prop': 'info', 'action': 'query', 'format': 'json',
#     'inprop': 'protection|watchers', 
#     'titles': '|'.join(schools)
#     }
#     resp = requests.get(baseurl, params = my_atts)
#     data = resp.json()
#     print data

# def my():

#     url = 'http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions'
#     tree  = html.fromstring(requests.get(url).text)
#     school_cells = tree.cssselect('table.wikitable')[0].cssselect('tr th:nth-of-type(1) a')
#     school_names = [t.text_content() for t in school_cells]
#     print school_names
# my()

# def my():

#     url = 'https://en.wikipedia.org/wiki/List_of_UTC_time_offsets'
#     tree  = html.fromstring(requests.get(url).text)
#     school_cells = tree.cssselect('table.wikitable')[0].cssselect('tr th:nth-of-type(1) a')
#     school_names = [t.text_content() for t in school_cells]
#     print school_names
# my()


# refer to: https://blog.scraperwiki.com/2011/12/how-to-scrape-and-parse-wikipedia/
####################################

def findUTC():
    H= datetime.datetime.utcnow().strftime("%H")
    intH= int(H)
    location = ""
    current = intH-17
    if current == 0:
        current = current
    else: 
        current *= -1
    print current
    if current == 0:
        location = "Greenwich"
    else:
        location = "FUCK"
        
    return location
# def scrapewiki():
#     return urllib.urlopen("http://en.wikipedia.org/wiki/Aquamole_Pot").read()

# def scrapewiki():
#     title = "Aquamole Pot"
#     params = { "format":"xml", "action":"query", "prop":"revisions", "rvprop":"timestamp|user|comment|content" }
#     params["titles"] = "API|%s" % urllib.quote(title.encode("utf8"))
#     qs = "&".join("%s=%s" % (k, v)  for k, v in params.items())
#     url = "http://en.wikipedia.org/w/api.php?%s" % qs
#     tree = lxml.etree.parse(urllib.urlopen(url))
#     revs = tree.xpath('//rev')

#     print "The Wikipedia text for", title, "is"
#     print revs[-1].text
    
# def scrapewiki():
#     wikipedia_utils = scraperwiki.utils.swimport("wikipedia_utils") ## ERRONEOUS

#     title = "Aquamole Pot"

#     val = wikipedia_utils.GetWikipediaPage(title)
#     res = wikipedia_utils.ParseTemplates(val["text"])
#     print res               # prints everything we have found in the text
#     infobox_ukcave = dict(res["templates"]).get("Infobox ukcave")
#     print infobox_ukcave    # prints just the ukcave infobox
# scrapewiki()

# def trywiki():
#     #UTCList= wikipedia.summary("List_of_UTC_time_offsets",sentences=1)
#     UTCList=wikipedia.page("UTC-12")
#     trythis=UTCList.content
#     print trythis
#     print UTCList.links


# def trywiki():
#     #url= "/https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
#     url = "https://en.wikipedia.org/wiki/List_of_ship_names_of_the_Royal_Navy_(A)"
#     wiki_html= urllib.urlopen(url)
#     soup = BeautifulSoup(wiki_html,"lxml")
    
#     links=soup.find_all("a")

#     for link in links:
#     	title = str(link.get("titles"))
#         print title

def trywiki():
    url= "https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
    urllist=[]
    wiki_html= urllib.urlopen(url)
    soup = BeautifulSoup(wiki_html,"lxml")
    
    links=soup.find_all("h2")
    print links
#    for link in links:
#        titles= str(link.get(""))
#         print titles
#     for link in links:
#     	title = str(link.get("titles"))
#         print title



# Create your views here.
def home(request):
    template= "home.html"
    now = datetime.datetime.now()
    test = str(now)
    realtime= test[11:]
    #print scrapewiki()
  #  print findUTC()
    
    
    
    
    context={
        "now": now,
    }
    return render(request,template,context) 