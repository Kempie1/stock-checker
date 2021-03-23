import psycopg2
import psycopg2.extras
import json
import requests
from json.decoder import JSONDecodeError

class Json_to_server():
    def open_json_file(self):
        with open('stock.json') as json_file:
            try:
                self.data = json.load(json_file)
            except ValueError:
                print('Decoding JSON has failed')
    
    def checking_if_ticker_exists(self):
        DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
        DB_NAME = "b8emsfkpxajppbmkv48x"
        DB_USER = "uazqb7phtgnjgeix5pcv" 
        DB_PASS = "5TwfUnm8z4bcGzmMjr4h"

        conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

        with conn: 
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT stock.ticker_symbol FROM stock")
                    self.ticker_table = cur.fetchall()

        json_ticker_symbol = self.data['symbol']
        self.ticker_symbol = "['" + json_ticker_symbol + "']"

        for i in range(len(self.ticker_table)):
            if self.ticker_symbol != str(self.ticker_table[i]):
                self.already_exists_in_DB = False

        for i in range(len(self.ticker_table)):
            if self.ticker_symbol == str(self.ticker_table[i]):
                print("This Ticker is already existing in the Database")
                self.already_exists_in_DB = True


    def connecting_to_server(self):
        
        DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
        DB_NAME = "b8emsfkpxajppbmkv48x"
        DB_USER = "uazqb7phtgnjgeix5pcv" 
        DB_PASS = "5TwfUnm8z4bcGzmMjr4h"

        conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        if self.already_exists_in_DB == False:
            with conn: 
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT stock.ticker_symbol FROM stock")
                    self.ticker_table = cur.fetchall()

                    cur.execute('''
                INSERT INTO stock (
                    ticker_symbol,
                    stock_name,
                    stock_price,
                    previous_close,
                    open
                ) values  (%s,%s,%s,%s,%s)
                returning stock
                ''', (
                    self.data['symbol'],
                    self.data['quoteType']['longName'],
                    self.data['price']['regularMarketPrice']['raw'],
                    self.data['summaryDetail']['regularMarketPreviousClose']['raw'],
                    self.data['price']['regularMarketOpen']['raw']
                )
            )
                    print(cur.fetchall())
                    print("Everything was added to the database")
                    
            conn.commit()
            conn.close()
        

server = Json_to_server()
server.open_json_file()
server.checking_if_ticker_exists()
server.connecting_to_server()

