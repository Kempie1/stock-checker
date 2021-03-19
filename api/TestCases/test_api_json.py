import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest

class test_Api(unittest.TestCase):

    def test_api_request(self):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            print(response)
            print(response.status_code)
            assert response.status_code == 200
        except requests.exceptions.HTTPError as err:
            print(err)

        #This is checking if the right input is coming in Video 2
        json_response = json.loads(response.text)
        ticker_symbol_from_API = jsonpath.jsonpath(json_response, 'symbol')
        print(ticker_symbol_from_API)
        assert ticker_symbol_from_API == ['TSLA']

        
        #new test
            #response = requests.post(url, request_json)
            #print(response.status_code)
            #assert response.status_code == 200
    
    def test_json(self):
        #Json file check Video 4
        with open('stock.json') as json_file:
            try:
                request_json = json.load(json_file)
            except ValueError:
                print('Decoding JSON has failed')

            ticker_symbol_json = jsonpath.jsonpath(request_json, 'symbol')
            print(ticker_symbol_json)
            assert ticker_symbol_json == ['TSLA']
                



Api_test = test_Api()
Api_test.test_api_request()

# TOP Playlist on youtube for Api tests https://www.youtube.com/watch?v=OdFW3RwAz8w&list=PLIMhDiITmNrILoYaVsrxwteH6LqMr07uX&index=5&ab_channel=TestingWorld
# If in the terminal I type pytest TestCases so the module and the folder name then  
#       In my class I need to write unittest.TestCase linke BELOW

# Link: https://stackoverflow.com/questions/34363388/pytest-no-tests-ran

#Some issues with requests post and requests put

#pytest TestCases

#pytest -v TestCases "WITH THIS I CAN SEE HOW LONG AND WHIHC TEST HAS FAILED"

