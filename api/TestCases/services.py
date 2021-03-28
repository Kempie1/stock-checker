# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import os

def get_todos():
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': "fd4a157371mshb331f054ae72222p1cefa5jsnd889b6441b08",
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
                if todos['symbol'] == 'TSLA':
                    completed = False
            
        return[todo]

#if todo('symbol') == "TSLA":
#                return[todo]

# This is now going into the fake.json and checking if one of the values is False as it should be in the predefined fake.json

get_uncompleted_todos()
get_todos()