import requests
import json
import psycopg2
import psycopg2.extras
import json
import os


class Api_call():

    def user_input(self):
        user_input = input("What stock would you like to see ")
        self.user_input_copy = user_input
        string_conversion = "['" + user_input + "']"
        self.ticker_symbol = string_conversion
        return self.ticker_symbol

    def connecting_to_server(self):
        DB_HOST = os.environ['DB_HOST']
        DB_NAME = os.environ['DB_NAME']
        DB_USER = os.environ['DB_USER']
        DB_PASS = os.environ['DB_PASS']
        
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

    def api_request(self):
        if self.already_exist == False:   
            url = os.environ['URL']
            querystring = {"symbol": self.user_input_copy,"region":"US"}
            headers = {
            'x-rapidapi-key': os.environ['APIKEY'],
            'x-rapidapi-host': os.environ['APIHOST']
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            self.response_string = response.text

    def api_request_to_json(self):
        if self.already_exist == False:    
            response_s = self.response_string
            file1 = open("stock.json","w") 
            file1.write(response_s)
            file1.close()
            print("Stock Data has been added to Json")
        if self.already_exist == True:
            file1 = open("stock.json", "w")
            file1.write("")
            file1.close()

Api = Api_call()
Api.user_input()
Api.connecting_to_server()
Api.checking_if_ticker_exists()
Api.api_request()
Api.api_request_to_json()


