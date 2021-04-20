import requests
import json
import psycopg2
import psycopg2.extras
import json
from decouple import config


class Api_call():

    def user_input(self, myinput):
        user_input = myinput("What stock would you like to see ")
        self.user_input_copy = user_input
        self.ticker_symbol = "['" + user_input + "']"
        return self.ticker_symbol


    def connecting_to_server(self):
        DB_HOST = config('DB_HOST')
        DB_NAME = config('DB_NAME')
        DB_USER = config('DB_USER')
        DB_PASS = config('DB_PASS')
        
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        
        with conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT stock.ticker_symbol FROM stock")
                self.ticker_symbol_table = cur.fetchall()
    
    def checking_if_ticker_exists(self):
        for i in range(len(self.ticker_symbol_table)):
            if self.ticker_symbol != str(self.ticker_symbol_table[i]):
                self.already_exist = False

        for i in range(len(self.ticker_symbol_table)):
            if self.ticker_symbol == str(self.ticker_symbol_table[i]):
                print("This Ticker is already existing in the Database")
                self.already_exist = True

        if len(self.ticker_symbol_table) == 0:
            print("There is nothing in the ticker_symbol Table")
            self.already_exist = False

    def api_request(self, request):
        if self.already_exist == False:
            url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
            querystring = {"symbol": self.user_input_copy,"region":"US"}
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

Api = Api_call()
Api.user_input(input)
Api.connecting_to_server()
Api.checking_if_ticker_exists()
Api.api_request_to_json(["get-statistics", "get-financials"])


