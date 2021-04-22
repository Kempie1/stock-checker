import requests
import json
import psycopg2
import psycopg2.extras
import json
from decouple import config
import sys

from ORM_services import connecting_to_server

class Api_call():

    def user_input(self, myinput):
        user_input = myinput("What stock would you like to see ")
        self.ticker_symbol = "['" + user_input + "']"
        return self.ticker_symbol

    def get_ticker_table_list(self):
        conn = connecting_to_server()

        with conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT stock.ticker_symbol FROM stock")
                self.ticker_symbol_table = cur.fetchall()
                return self.ticker_symbol_table
    
    def checking_if_ticker_exists(self, ticker_symbol_table):
        for i in range(len(ticker_symbol_table)):
            if self.ticker_symbol != str(ticker_symbol_table[i]):
                self.already_exist = False
    
        for i in range(len(ticker_symbol_table)):
            if self.ticker_symbol == str(ticker_symbol_table[i]):
                print("This Ticker is already existing in the Database")
                self.already_exist = True

        if len(ticker_symbol_table) == 0:
            print("There is nothing in the ticker_symbol Table")
            self.already_exist = False

        return self.already_exist

    def api_request(self, request):
        if self.already_exist == False:
            url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
            querystring = {"symbol": self.ticker_symbol,"region":"US"}
            headers = {
            'x-rapidapi-key': config('APIKEY'),
            'x-rapidapi-host': config('APIHOST')
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response.text

    #def api_request_to_json(self,request):
     #   if self.already_exist == False:    
      #      file1 = open(f"{request}.json","w") 
       #     file1.write(api_request(request))
        #    file1.close()
         #   print("Stock Data has been added to Json")
        #if self.already_exist == True:
         #   file1 = open(f"{request}.json", "w")
          #  file1.write("")
           # file1.close()

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

#Api = Api_call()
#Api.user_input(input)
#Api.get_ticker_table_list()
#Api.checking_if_ticker_exists(Api.get_ticker_table_list())
#Api.api_request_to_json(["get-statistics", "get-financials"])


