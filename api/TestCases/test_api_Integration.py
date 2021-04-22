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
from constants import ticker_symbol_for_testing, ticker_symbol_for_request

class test_Api(unittest.TestCase):

    def test_api_request_status(self):
        #Both Work on either side same thing
        #Given / Arrange (OPTIONAL)
        constant_input = ticker_symbol_for_request
        #When / Act 
        response = get_todos()
        #Then / Assert
        self.assertEqual(response.status_code, 200)
        
    def test_api_data(self):
        #Arrange
        constant_input = ticker_symbol_for_request
        #Act
        response = get_todos()
        json_response = json.loads(response.text)
        ticker_symbol_from_API = jsonpath.jsonpath(json_response, 'symbol')
        #Assert
        self.assertEqual(ticker_symbol_from_API, constant_input)
    
    def test_json_data(self):
        #Arrange
        constant_input = ticker_symbol_for_testing
        #Act
        with open('TestCases/teststock.json') as json_file:
            request_json = json.load(json_file)
            ticker_symbol_json = request_json['get-statistics']['symbol']
        #Assert    
            assert ticker_symbol_json == constant_input
                
if __name__ == '__main__':
    unittest.main()

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
Api_test.test_api_request_status()
Api_test.test_api_data()
Api_test.test_json_data()

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