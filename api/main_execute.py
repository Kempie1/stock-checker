import requests
import json
import psycopg2
import psycopg2.extras
import json

#Main
from ORM.api_call_to_json import Api_call
from ORM.json_to_server import Json_to_server
from ORM.ORM_services import connecting_to_server

#Test
#from TestCases.test_api import test_Api_python_file

class Execute:
    def __init__(self):
        self.Api = Api_call()
        self.Server = Json_to_server()
        self.Api_test = test_Api_python_file()

    def execute_api(self,ticker):
        self.Api.user_input(input)
        self.Api.get_ticker_table_list()
        self.Api.checking_if_ticker_exists(Api.get_ticker_table_list())
        self.Api.api_request_to_json(["get-statistics", "get-financials"])

    def execute_server(self):
        self.Server.open_json_file()
        self.Server.checking_if_ticker_exists()
        self.Server.connecting_to_server()

    def execute_tests(self):
        print("")
        #self.Api_test.test_api()
        

main = Execute()
#main.execute_api()
#main.execute_tests()
main.execute_server()

