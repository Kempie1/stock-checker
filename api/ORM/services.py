# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import os
import unittest
from constants import ticker_symbol_for_testing

def real_api_request():
        ticker_symbol = ticker_symbol_for_testing
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": ticker_symbol,"region":"US"}
        headers = {
        'x-rapidapi-key': "92e0efc621msh368787aa782ea71p111f83jsn3acbf2f81995",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.ok:
            return response
        else:
            return None
            #If request fails then nothing will be returned

#Link: https://realpython.com/testing-third-party-apis-with-mocks/

def get_uncompleted_todos():
    response = get_todos()
    if response is None:
        return []
    else:
        todos = response.json()
        for todo in todos: 
            if todo == 'symbol':
                if todos['symbol'] == 'CSV':
                    completed = False
            
        return[todo]

#if todo('symbol') == "TSLA":
#                return[todo]

# This is now going into the fake.json and checking if one of the values is False as it should be in the predefined fake.json

