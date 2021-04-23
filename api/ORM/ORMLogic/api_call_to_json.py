import requests
import json
import psycopg2
import psycopg2.extras
import json
from decouple import config
import sys

from ORM_services import ORM_services

class Api_call():

    def user_input(self, myinput):
        user_input = myinput
        self.ticker_symbol = "['" + user_input + "']"
        return self.ticker_symbol

    def checking_if_ticker_exists_in_database(self):
        self.services = ORM_services()
        ticker_symbol = ["TSLA"]
        self.already_exist = self.services.checking_if_ticker_exists(ticker_symbol)
        print(self.already_exist)

    def api_request(self, request):
        if self.already_exist == False:
            #self.services.api_request(["get-statistics", "get-financials"], ["TSL"])
            url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
            querystring = {"symbol": ["TSL"],"region":"US"}
            headers = {
            'x-rapidapi-key': config('APIKEY'),
            'x-rapidapi-host': config('APIHOST')
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response.text

    def api_request_to_json(self, request):
        if self.already_exist == False:
            file1 = open("stock.json","w") 
            for x in range(len(request)):
                if x==0:
                    file1.write(f"{{\"{request[x]}\": " + self.api_request(request[x]))
                else:
                    file1.write(f",\"{request[x]}\": " + self.api_request(request[x]))
            file1.write("}")
            file1.close()
            print("Stock Data has been added to Json")
        if self.already_exist == True:
            file1 = open(f"stock.json", "w")
            file1.write("")
            file1.close()

Api = Api_call()
#Api.user_input("TSLA")
Api.checking_if_ticker_exists_in_database()
#Api.api_request_to_json(["get-statistics", "get-financials"])


