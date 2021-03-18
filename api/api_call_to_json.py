import requests
import json
import psycopg2
import psycopg2.extras
import json

class Api_call:

    def user_input(self):
        user_input = input("What stock would you like to see ")
        string_conversion = "['" + user_input + "']"
        self.ticker_symbol = string_conversion

    def connecting_to_server(self):
        DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
        DB_NAME = "b8emsfkpxajppbmkv48x"
        DB_USER = "uazqb7phtgnjgeix5pcv" 
        DB_PASS = "5TwfUnm8z4bcGzmMjr4h"
        
        conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        
        with conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT stock.ticker_symbol FROM stock")
                self.ticker_symbol_table = cur.fetchall()
    
    def checking_if_ticker_exists(self):
        for i in range(len(self.ticker_symbol_table)):
            if self.ticker_symbol == str(self.ticker_symbol_table[i]):
                print("This Ticker is already existing in the Database")
            else:
                p1.api_request()
                #p1.api_request_to_json()

    def api_request(self):
        print(self.ticker_symbol)
        print(self.ticker_symbol.replace('', '['))
        #url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        #querystring = {"symbol": "AAPL","region":"US"}
        #headers = {
       # 'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
       # 'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
       # }
       # response = requests.request("GET", url, headers=headers, params=querystring)
       # self.response_string = response.text

    def api_request_to_json(self):
        print(self.response_string)
        response_string = self.response_string
        print(response_string)
        file1 = open("stock.json","w") 
        file1.write(response_string)
        file1.close()


p1 = Api_call()
p1.user_input()
p1.connecting_to_server()
p1.checking_if_ticker_exists()


