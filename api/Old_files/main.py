#Server Connection Creditals
DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
DB_NAME = "b8emsfkpxajppbmkv48x"
DB_USER = "uazqb7phtgnjgeix5pcv" 
DB_PASS = "5TwfUnm8z4bcGzmMjr4h"

#Import
import psycopg2
import psycopg2.extras
import json

#Connecting to server
conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

#Opening Json file
with open('stock.json') as json_file:
    data = json.load(json_file)

#In the Curosur I am now executeing an SQL statement
#Executing SQL Statements

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
        data['symbol'],
        #str(data["FOB_currency"]),
        data['quoteType']['longName'],
        data['price']['regularMarketPrice']['raw']
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
        data['symbol'],
        data['summaryDetail']['regularMarketPreviousClose']['raw'],
        data['price']['regularMarketOpen']['raw']
    )
)

        print(cur.fetchall())
        
conn.commit()
conn.close()