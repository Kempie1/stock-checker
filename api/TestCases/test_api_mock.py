#import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest

from nose.tools import assert_true
import requests

class test_api_mock(unittest.TestCase):
    
     def test_request_response(self):

        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": "TSLA","region":"US"}
        headers = {
        'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        # Send a request to the API server and store the response.
        response = requests.get(url, headers=headers, params=querystring)
        # Confirm that the request-response cycle completed successfully.
        assert_true(response.ok)
 
    
        


Api_test_mock = test_api_mock()
Api_test_mock.test_request_response()
