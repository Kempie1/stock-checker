import requests
import json
import psycopg2
import psycopg2.extras
import json

from api_call_to_json import Api_call
from json_to_server import Json_to_server
from TestCases.test_api_json import test_Api

class Execute:
    def __init__(self):
        self.Api = Api_call()
        self.Server = Json_to_server()
        self.Api_test = test_Api()

    def execute_api(self):
        self.Api.user_input()
        self.Api.connecting_to_server()
        self.Api.checking_if_ticker_exists()
        self.Api.api_request()
        self.Api.api_request_to_json()

    def execute_server(self):
        self.Server.open_json_file()
        self.Server.checking_if_ticker_exists()
        self.Server.connecting_to_server()

    def execute_api_tests(self):
        print("Nothing yet")

main = Execute()
main.execute_api()
main.execute_server()
main.execute_api_tests()
