import requests
import json
import psycopg2
import psycopg2.extras
import json


class Api_call():

    def user_input(self):
        user_input = input("What stock would you like to see ")
        self.user_input_copy = user_input
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
            if self.ticker_symbol != str(self.ticker_symbol_table[i]):
                self.already_exists = False

        for i in range(len(self.ticker_symbol_table)):
            if self.ticker_symbol == str(self.ticker_symbol_table[i]):
                print("This Ticker is already existing in the Database")
                self.already_exists = True
             
            
    def api_request(self):
        if self.already_exists == False:   
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
            querystring = {"symbol": self.user_input_copy,"region":"US"}
            headers = {
            'x-rapidapi-key': "7457cdc0c7msh99dadc0f2dd0fe9p15e2b1jsn8609005a4aa7",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            self.response_string = response.text

    def api_request_to_json(self):
        if self.already_exists == False:    
            response_s = self.response_string
            file1 = open("stock.json","w") 
            file1.write(response_s)
            file1.close()
            print("Stock Data has been added to Json")
        if self.already_exists == True:
            file1 = open("stock.json", "w")
            file1.write("")
            file1.close()

Api = Api_call()
Api.user_input()
Api.connecting_to_server()
Api.checking_if_ticker_exists()
Api.api_request()
Api.api_request_to_json()


