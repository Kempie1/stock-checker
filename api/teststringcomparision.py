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
        #need returning stock for fetch
 
        cur.execute("SELECT stock.ticker_symbol FROM stock")

        check = cur.fetchall()

        print(check)
      
conn.commit() #This is helping to say if something is double like a table or so on

conn.close()


mylist=[]
#stock_input = input("What stock would you like to see ")
#mylist.append(stock_input)



print(check[0])

print(len(check))

for i in range(len(check)):
    #print(i)
    print(str(check[i])) 

     title[title._index['name']] = foo

    if mylist[0] == str(check[i]):
        print("WORKS")


print(mylist[0])