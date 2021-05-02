#External
import requests
import json
import psycopg2
import psycopg2.extras
import json
import sys
sys.path.append('/Users/maximilianhues/Documents/CODE/TESTCheckerTEST/stock-checker/api/ORM/ORMLogic')
sys.path.append('/Users/maximilianhues/Documents/CODE/TESTCheckerTEST/stock-checker/api/ORM')

#Internal
from ORM.ORMLogic.api_call_to_json import Api_call
from ORM.ORMLogic.json_to_server import Json_to_server
from ORM.ORMLogic.ORM_services import ORM_services

class Execute:
    def __init__(self):
        self.Api = Api_call()
        self.Server = Json_to_server()

    def user_input(self, myinput):
        self.ticker_symbol = myinput
        return self.ticker_symbol

    def execute_api(self):
        self.Api.checking_if_ticker_exists_in_database(self.ticker_symbol)
        self.Api.api_request_to_json(["get-statistics", "get-financials", "get-chart"])

    def execute_server(self):
        if self.Server.open_json_file('stock.json'):
            self.Server.send_data_to_server()
        

main = Execute()
main.user_input("F")
main.execute_api()
main.execute_server()


