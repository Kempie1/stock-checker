#External
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
import requests
import os
import unittest
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
import sys
sys.path.append(config('ORM'))
sys.path.append(config('ORMLogic'))
sys.path.append(config('MockFolder'))
sys.path.append(config('APIFOLDER'))
#Internal
from declarative import Stock, Base
from constants import ticker_symbol_for_testing

def mock_api_request():
    response = requests.get("http://127.0.0.1:5000/json")
    return response

def mock_third_party_api_request(request):
    response = requests.get(f"http://127.0.0.1:4000/{request}")
    return response

def real_api_request():
    response = requests.get(f"https://stockcheckerdb.herokuapp.com/getst/?ticker={ticker_symbol_for_testing}")
    return response

def third_party_api_request(request):
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
    querystring = {"symbol": ticker_symbol_for_testing,"region":"US"}
    headers = {
    'x-rapidapi-key': config("APIKEY"),
    'x-rapidapi-host': config("APIHOST")
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.ok:
        return response
    else:
        return None

def real_sql_request():
    #This is creating an engine connected to the Database URL
    #engine = create_engine(config("DB_URL"))
    #Base.metadata.bind = engine
    #DBSession = sessionmaker()
    #DBSession.bind = engine
    #session = DBSession()
   # engine = create_engine(config("DB_URL"))
    #Base.metadata.bind = engine
    #session = sessionmaker(bind=engine)
    #session.query(Stock).all()
    print("")