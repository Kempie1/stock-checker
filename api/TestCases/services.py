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
        'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
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
        #print(todos)
        return [todo for todo in todos if todo['completed'] == False]

# This is now going into the fake.json and checking if one of the values is False as it should be in the predefined fake.json

get_uncompleted_todos()
get_todos()