from django.shortcuts import render
####################################
import datetime # FOR FINDING UTC TIME
####################################
####################################
# FOR SCRAPING WIKI ##################
import urllib, urllib2
# import lxml.etree
# #import wikipedia
# #import scraperwiki
# from bs4 import BeautifulSoup
# from utils import *
# import requests
# from lxml import html
import json 
import random
################
from registration import signals
from registration.models import RegistrationProfile
from registration.views import ActivationView as BaseActivationView
from registration.views import RegistrationView as BaseRegistrationView
from registration.users import UserModel

###############


def findUTC():
    H= datetime.datetime.utcnow().strftime("%H")
    intH= int(H)
    current = (intH-17)
    return current


def countryData():
    ## START FROM -11
    utcMatrix=[["United States", "New Zealand"],
    ["France", "New Zealand", "United States"],
    ["France", "United States"],
    ["Canada", "France", "Mexico", "United Kingdom", "United States"],
    ["Canada", "Mexico", "United States"],
    ["Belize", "Canada", "Chile", "Costa Rica", "Ecuador", "El Salvador", "Guatemala", "Honduras", "Mexico", "Nicaragua", "United States"],
    ["Bahamas", "Brazil", "Canada", "Colombia", "Cuba", "Ecuador", "Haiti", "Jamaica", "Mexico", "Panama", "Peru", "United Kingdom", "United States"],
    ["Antigua and Barbuda", "Barbados", "Bolivia", "Brazil", "Canada", "Chile", "Denmark", "Dominica", "Dominican Republic", "France", "Grenada", "Guyana", "Netherlands", "Paraguay", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United Kingdom", "United States", "Venezuela"],
    ["Argentina", "Brazil", "Denmark", "France", "Suriname", "United Kingdom", "Uruguay"],
    ["Brazil", "United Kingdom"],
    ["Cape Verde", "Denmark", "Portugal"],
    ["Burkina Faso", "Cote d'Ivoire", "Denmark", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Iceland", "Republic of Ireland", "Liberia", "Mali", "Mauritania", "Morocco", "Portugal", "Sahrawi Republic", "Sao Tome and Principe", "Spain", "Senegal", "Sierra Leone", "Togo", "United Kingdom"],
    ["Albania", "Algeria", "Andorra", "Angola", "Austria", "Belgium", "Benin", "Bosnia and Herzegovina", "Cameroon", "Central African Republic", "Chad", "Republic of the Congo", "Democratic Republic of the Congo", "Croatia", "Czech Republic", "Denmark", "Equatorial Guinea", "France", "Gabon", "Germany", "Hungary", "Italy", "Kosovo", "Liechtenstein", "Luxembourg", "Republic of Macedonia", "Malta", "Monaco", "Montenegro", "Namibia", "Netherlands", "Niger", "Nigeria", "Norway", "Poland", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Tunisia", "United Kingdom", "Vatican City"],
    ["Botswana", "Bulgaria", "Burundi", "Cyprus", "Democratic Republic of the Congo", "Egypt", "Estonia", "Finland", "Greece", "Israel", "Jordan", "Latvia", "Lebanon", "Lesotho", "Lithuania", "Libya", "Malawi", "Moldova", "Mozambique", "State of Palestine", "Romania", "Russia", "Rwanda", "South Africa", "Swaziland", "Syria", "Turkey", "Ukraine", "United Kingdom", "Zambia", "Zimbabwe"],
    ["Bahrain", "Belarus", "Comoros", "Djbouti", "Eritrea", "Ethiopia", "France", "Georgia", "Iraq", "Kenya", "Kuwait", "Madagascar", "Qatar", "Russia","Saudi Arabia", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Uganda", "Ukraine", "Yemen"],
    ["Armenia","Azerbaijan","France", "Georgia","Iran", "Mauritius", "Oman", "Russia", "Seychelles", "United Arab Emirates"],
    ["Afghanistan", "Australia", "France", "Kazakhstan", "Maldives", "Pakistan", "Russia", "Tajikistan", "Turkmenistan", "Uzbekistan"],
    ["Bangladesh", "Bhutan", "India","Kazakhstan", "Kyrgyzstan", "Nepal", "Russia", "Sri Lanka", "United Kingdom"],
    ["Australia", "Cambodia", "Indonesia", "Laos", "Mongolia", "Myanmar", "Russia", "Thailand", "Vietnam"],
    ["Australia", "Brunei", "China", "Indonesia", "Malaysia", "Mongolia", "Philippines", "Russia", "Singapore", "Taiwan"],
    ["Australia", "Indonesia", "Japan", "North Korea", "South Korea", "Palau", "Russia", "Timor-Leste"],
    ["Australia", "Federated States of Micronesia", "Papua New Guinea", "Russia", "United States"],
    ["Australia", "Federated States of Micronesia", "France", "Papua New Guinea", "Russia", "Solomon Islands", "Vanuatu"],
    ["France", "Fiji", "Kiribati", "Marshall Islands", "Nauru", "New Zealand", "Russia", "Tuvalu", "United States"],
    ["Kiribati", "New Zealand", "Samoa", "Tonga"],
    ["Kiribati"]]
    return utcMatrix



 
  #url= "/https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
#     url = "https://en.wikipedia.org/wiki/List_of_ship_names_of_the_Royal_Navy_(A)"
#     wiki_html= urllib.urlopen(url)
#     soup = BeautifulSoup(wiki_html,"lxml")
    
 
   
# def john():
#     url= "https://en.wikipedia.org/wiki/List_of_UTC_time_offsets"
#     r = requests.get(url)
#     # r = urllib.urlopen(url)
#     soup= BeautifulSoup(r.content,"lxml")
#     # soup= BeautifulSoup(r,"lxml")

#     links = soup.find_all("a")
#     # for link in links:
#     #     print link.text

#     g_data = soup.find_all("span", {"id": "UTC.E2.88.9211:00.2C_X"})
#     print g_data
# john()

# def amelia():
#     currentUTC= str(findUTC())
#     print currentUTC
#     htmltext= urllib.urlopen("https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json")
#     #https://raw.githubusercontent.com/moment/moment-timezone/develop/data/meta/latest.json
#     data = json.load(htmltext)
#     targetlist = []
#     for zones in xrange(len(data)):
#         utcs= data[zones]['text']
#        # print str(utcs)
#         wow= str(utcs)[5:7]
        
#         if wow == currentUTC:
#             print "these are the places:", utcs
#             targetlist.append(utcs)
#    # print targetlist
#     return targetlist
            
def amelia():
    currentUTC = findUTC()
    #print "SHITSHITSHIT", currentUTC
    #print countryData()[11+currentUTC]
    randomCountry =  random.choice(countryData()[11+currentUTC])
    print "RAMDOMIZED#######", randomCountry
    return countryData()[11+currentUTC]
    

def drink():
    return { "Albania": "rakia",
    "Argentina": "fernet",
    "Armenia": "oghi",
    "Australia": "Bundaberg",
    "Austria": "schnapps",
    "Barbados": "rum",
    "Belarus": "krambambula",
    "Belgium": "jenever",
    "Belize": "rum",
    "Bermuda": "Black Seal Rum",
    "Bolivia": "singani",
    "Bosnia": "Rakija",
    "Herzegovina": "Rakija",
    "Brazil": "caipirinha",
    "Bulgaria": "rakia",
    "Cambodia": "sombai",
    "Canada": "Canadian rye whisky",
    "Chile": "pisco",
    "China": "moutai",
    "Colombia": "aguardiente",
    "Costa Rica": "guaro",
    "Croatia": "rakija",
    "Cuba": "Havana Club",
    "Czech Republic": "Becherovka",
    "Denmark": "akvavit",
    "Dominican Republic":"mamjuana",
    "Ecuador": "aguardiente",
    "El Salvador": "Torito",
    "Estonia":"Vana Tallinn",
    "Ethiopia": "tej",
    "Finland":"Koskenkorva Viina",
    "France": "Champagne",
    "French West Indies": "rum",
    "Georgia": "chacha",
    "Germany": "Schnapps",
    "Ghana":"akpeteshie",
    "Greece": "ouzo",
    "Guatemala":"Ron Zacapa Centenario",
    "Haiti":"Rhum Barbancourt",
    "Hungary":"Unicum",
    "Iceland":"Brennivin",
    "India":"feni",
    "Indonesia":"arrack",
    "Iran":"aragh",
    "Iraq":"arak",
    "Ireland":"Irish whiskey",
    "Israel":"arak",
    "Italy": "grappa",
    "Jamaica":"rum",
    "Japan": "sake",
    "Jordan":"arak",
    "Kenya":"dawa",
    "Korea":"soju",
    "Latvia":"balsam",
    "Lebanon":"anise",
    "Levant":"arak",
    "Macedonia":"rakija",
    "Malaysia":"tuak",
    "Mexico":"tequila",
    "Montenegro":"rakija",
    "Nepal":"raksi",
    "Netherlands":"jenever",
    "Nicaragua":"rum",
    "Norway":"akevitt",
    "Panama":"Seco Herrerano",
    "Peru":" pisco",
    "Philippines":"lambanog",
    "Poland":"Mead",
    "Portugal":"ginjinha",
    "Puerto Rico":"pitorro",
    "Romania":"palinka",
    "Russia":"vodka",
    "Serbia":"rakija",
    "Slovakia":"borovicka",
    "South Afrika":"Amarula",
    "South Korea":"Soju",
    "Spain":"sherry",
    "Sri Lanka":"arrack",
    "Sweden":"brannvin",
    "Switzerland":"absinthe",
    "Syria":"arak",
    "Taiwan":"kaoliang",
    "Tanzania":"konyagi",
    "Thailand":"Mekhong whiskey",
    "Trinidad and Tobago":"rum",
    "Tunisia":"boukha",
    "Turkey":"raki",
    "Uganda":"waragi",
    "Ukraine":"horilka",
    "United Kingdom":"Gin",
    "United States":"Bourbon",
    "Venezuela":"rum",
    "Vietnam":"snake wine"
    }
    

# Create your views here.
def home(request):
    template= "homepage_templates/home.html"
    now = datetime.datetime.now()
    test = str(now)
    realtime= test[11:]
    #print scrapewiki()
  #  print findUTC()
    randomCountry = random.choice(amelia())
    drinkcountry= randomCountry
    try:
        Drink= drink()[drinkcountry]
    except: 
        Drink = "This country does not have any national drink in our database"
    newamelia=amelia()
    
    
    
    
    context={
        "now": now,
        "amelia":newamelia,
        "randomCountry": randomCountry,
        "Drink":Drink,
    }
    return render(request,template,context) 