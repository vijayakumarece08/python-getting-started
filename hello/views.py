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


    # Get VIX value using NSEPy Package
def get_vix_value():
    print ("Inside Vix  - Hello World");
    # Assume yesterday as today
    yesterday = date.today();
    while True:
        # Get yesterday date as we are going to run this before market hours
        yesterday = yesterday;

        # Get VIX value of yesterday
        df = pd.DataFrame(nsepy.get_history(symbol="INDIAVIX", start=yesterday, end=yesterday, index=True));
        # IF no data found on yesterday, go back to previous day because it may be weekend
        if (df.empty == False):
            break

    # Return VIX value based on close
    return df.iloc[1][3]

def index(request):
    print ("Inside Index  - Hello World");
    get_vix_value();
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
