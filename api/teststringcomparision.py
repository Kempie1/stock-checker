#Server Connection Creditals
DB_HOST = "b8emsfkpxajppbmkv48x-postgresql.services.clever-cloud.com"
DB_NAME = "b8emsfkpxajppbmkv48x"
DB_USER = "uazqb7phtgnjgeix5pcv" 
DB_PASS = "5TwfUnm8z4bcGzmMjr4h"

#Import
import psycopg2
import psycopg2.extras
import json

conn = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

with conn: 
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT stock.ticker_symbol FROM stock")
        check = cur.fetchall()
        print(check)
      
conn.commit()
conn.close()

mylist=[]
stock_input = input("What stock would you like to see ")
stock_input2 = "['" + stock_input + "']"
mylist.append(stock_input)

print(stock_input2)

for i in range(len(check)):
    if stock_input2 == str(check[i]):
        print("WORKS")


