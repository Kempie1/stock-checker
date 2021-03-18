import psycopg2
import psycopg2.extras
import json
import requests

class Json_to_server:
    def open_json_file(self):
        with open('stock.json') as json_file:
            self.data = json.load(json_file)
    
    def connecting_to_server(self):
        
        DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
        DB_NAME = "b8emsfkpxajppbmkv48x"
        DB_USER = "uazqb7phtgnjgeix5pcv" 
        DB_PASS = "5TwfUnm8z4bcGzmMjr4h"
        
        conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        
        with conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                
                cur.execute('''
            INSERT INTO stock (
                ticker_symbol,
                stock_name,
                stock_price
            ) values  (%s,%s,%s)
            returning stock
            ''', (
                self.data['symbol'],
                self.data['quoteType']['longName'],
                self.data['price']['regularMarketPrice']['raw']
            )
        )
                print(cur.fetchall())
                
                cur.execute('''
            INSERT INTO stock_summary (
                ticker_symbol,
                previous_close,
                open
            ) values  (%s,%s,%s)
            returning stock_summary
            ''', (
                self.data['symbol'],
                self.data['summaryDetail']['regularMarketPreviousClose']['raw'],
                self.data['price']['regularMarketOpen']['raw']
            )
        )

                print(cur.fetchall())
                
        conn.commit()
        conn.close()

        

p1 = Json_to_server()
p1.open_json_file()
p1.connecting_to_server()
