from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import nsepy
from datetime import date
import pandas as pd

# Create your views here.
#def index(request):
    # return HttpResponse('Hello from Python!')
 #   return render(request, "index.html")

print ("Inside Views - Hello World");


#from kiteconnect import KiteConnect
#import os
#import datetime as dt
#import pandas as pd

#cwd = os.chdir("C:/Users/hozef/OneDrive/Desktop/New Logic")

#generate trading session
#access_token = open("access_token.txt",'r').read()
#key_secret = open("api_key.txt",'r').read().split()
#kite = KiteConnect(api_key=key_secret[0])
#kite.set_access_token(access_token)


#get dump of all NSE instruments
#instrument_dump = kite.instruments("NSE")
#instrument_df = pd.DataFrame(instrument_dump)
#print (instrument_df)



    # Get VIX value using NSEPy Package
def get_vix_value():
    #pd.set_option("display.max_rows", None, "display.max_columns", None);
    print ("Inside Vix  - Hello World");
    

    # Assume yesterday as today
    yesterday = date.today();
    #while True:
        # Get yesterday date as we are going to run this before market hours
        #yesterday = yesterday;

        # Get VIX value of yesterday
    df = pd.DataFrame(nsepy.get_history(symbol="INDIAVIX", start=date(2015,1,1), end=date(2015,1,10), index=True));
    #df;
    #print ("after");
        # IF no data found on yesterday, go back to previous day because it may be weekend
     #   if (df.empty == False):
      #      break

     #Return VIX value based on close
    #print (df);
    return ("success - VIX - Option Selling");

def index(request):
    print ("Inside Index  - Hello World");    
    
    from py5paisa import FivePaisaClient
    client = FivePaisaClient(email="lakshmifemina7@gmail.com", passwd="Vinayakk@123", dob="19920710")
    client.login()
    req_list_=[{"Exch":"N","ExchType":"D","Symbol":"NIFTY 22 APR 2021 CE 15200.00","Expiry":"20210422","StrikePrice":"15200","OptionType":"CE"},
            {"Exch":"N","ExchType":"D","Symbol":"NIFTY 22 APR 2021 PE 15200.00","Expiry":"20210422","StrikePrice":"15200","OptionType":"PE"}]

    client.fetch_market_feed(req_list_)
    print(client.fetch_market_feed(req_list_))
    
    # Fetches holdings
    print(client.holdings())

    # Fetches margin
    client.margin()

    # Fetches positions
    client.positions()

    # Fetches the order book of the client
    print(client.order_book())

    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + "........ I love my dear Nagalakshmi......." +'</pre>')

#print (get_vix_value());

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
