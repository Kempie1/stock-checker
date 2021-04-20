import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
import sys
sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api')
from services import get_todos, get_uncompleted_todos
from constants import ticker_symbol_for_testing
from api_call_to_json import user_input

#I need to have a constant stockTest.json file 
#Variables should not change they should be constant in test

class test_Api(unittest.TestCase):

    def test_api_request(self):
        #Both Work on either side same thing
        #Given / Arrange (OPTIONAL)
        self.input = ticker_symbol_for_testing
        #When / Act 
        response = get_todos()
        #Then / Assert
        self.assertEqual(response.status_code, 200)
        
        #This is checking if the right input is coming in Video 2
        json_response = json.loads(response.text)
        #This is checking if in the response the 'symbol' string is existing
        ticker_symbol_from_API = jsonpath.jsonpath(json_response, 'symbol')
        
        #This string modfying is WEIRD
        modifiedinput = "['" + self.input + "']"
        ticker_symbol_from_API = f"{ticker_symbol_from_API}"
        
        print(ticker_symbol_from_API)
        print(modifiedinput)
        self.assertEqual(ticker_symbol_from_API, modifiedinput)
    
    def test_json(self):
        self.input = ticker_symbol_for_testing
        #Json file check Video 4
        with open('stock.json') as json_file:
            try:
                request_json = json.load(json_file)
            except ValueError and AttributeError:
                print('Decoding JSON has failed')

            ticker_symbol_json = request_json['get-statistics']['symbol']
            print(ticker_symbol_json)
            print(self.input)
            assert ticker_symbol_json == self.input 
                


#dependcy injection
#This is now giving a return to the function

    def test_user_input(self):
        #Act
        ticker_symbol_from_user = user_input(self.mock_input)
        #Assert
        self.assertEqual(ticker_symbol_from_user, "['Some User Input']")

    def mock_input(self,_):
        return "Some User Input"


Api_test = test_Api()
Api_test.test_api_request()
Api_test.test_json()

# TOP Playlist on youtube for Api tests https://www.youtube.com/watch?v=OdFW3RwAz8w&list=PLIMhDiITmNrILoYaVsrxwteH6LqMr07uX&index=5&ab_channel=TestingWorld
# If in the terminal I type pytest TestCases so the module and the folder name then  
#       In my class I need to write unittest.TestCase linke BELOW

# Link: https://stackoverflow.com/questions/34363388/pytest-no-tests-ran

#Some issues with requests post and requests put

#pytest TestCases

#pytest -v TestCases "WITH THIS I CAN SEE HOW LONG AND WHIHC TEST HAS FAILED"

#Professor told me to do: 

#Checks if the json is correct
# Calls the thrid party api and check if it has the correct response
# Mock thridparty api 
#  Need a framwork for testing (pytest)