import requests
import json
import psycopg2
import psycopg2.extras
import json
from decouple import config
import sys

from ORM_services import ORM_services

class Api_call():

    def checking_if_ticker_exists_in_database(self, ticker_symbol):
        self.services = ORM_services()
        self.ticker_symbol = ticker_symbol
        self.already_exist = self.services.checking_if_ticker_exists(ticker_symbol, ['REALCASE'])
        print(self.already_exist)
        return self.already_exist

    def api_request_to_json(self,request):
        if self.already_exist == False:
            file1 = open("stock.json","w") 
            for x in range(len(request)):
                if x==0:
                    file1.write(f"{{\"{request[x]}\": " + self.services.api_request(request[x], self.ticker_symbol))
                else:
                    file1.write(f",\"{request[x]}\": " + self.services.api_request(request[x], self.ticker_symbol))
            file1.write("}")
            file1.close()
            print("Stock Data has been added to Json")
        if self.already_exist == True:
            file1 = open(f"stock.json", "w")
            file1.write("")
            file1.close()


