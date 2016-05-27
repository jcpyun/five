from django.shortcuts import render
####################################
import datetime # FOR FINDING UTC TIME
####################################
####################################
# FOR SCRAPING WIKI ##################
import urllib, urllib2
from lxml import etree  
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

def scrapewiki():
    title = "Aquamole Pot"
    params = { "format":"xml", "action":"query", "prop":"revisions", "rvprop":"timestamp|user|comment|content" }
    params["titles"] = "API|%s" % urllib.quote(title.encode("utf8"))
    qs = "&".join("%s=%s" % (k, v)  for k, v in params.items())
    url = "http://en.wikipedia.org/w/api.php?%s" % qs
    tree = lxml.etree.parse(urllib.urlopen(url))
    revs = tree.xpath('//rev')

    print "The Wikipedia text for", title, "is"
    print revs[-1].text
scrapewiki()
# Create your views here.
def home(request):
    template= "home.html"
    now = datetime.datetime.now()
    test = str(now)
    realtime= test[11:]
    print scrapewiki()
    print findUTC()
    
    
    
    
    context={
        "now": now,
    }
    return render(request,template,context) 