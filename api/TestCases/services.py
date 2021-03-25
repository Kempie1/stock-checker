# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import os

def get_todos():
        url = os.environ['URL']
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': os.environ['APIKEY'],
        'x-rapidapi-host': os.environ['APIHOST']
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.ok:
            return response
        else:
            return None
            #If request fails then nothing will be returned


get_todos()

#Link: https://realpython.com/testing-third-party-apis-with-mocks/