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

with open('stock.json') as json_file:
    data = json.load(json_file)
    
    print(data['price']['regularMarketPrice'])
    print(data['price']['regularMarketPrice']['raw'])
    print(data['price']['currency'])

    for price in data['price']:
        
        #print(price)
       # print(price)
        if price == 'currency':
            print(price)
  
        #print('Name: ' + p['name'])
        #print('Website: ' + p['website'])
        #print('From: ' + p['from'])
        #print('')

    test = data['price']['regularMarketPrice']['raw']
    print(test)

#In the Curosur I am now executeing an SQL statement
#Executing SQL Statements

with conn: #With conn: This will ensure it is connecting
    #With: will make sure that it is connection to the cursour
    #This will close cursour automatically
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("INSERT INTO student (name) VALUES(%s)", (data['price']['regularMarketPrice']['raw'],))
        cur.execute("SELECT * FROM student;")
        print(cur.fetchall())

conn.commit() #This is helping to say if something is double like a table or so on

conn.close()

#At the top I selected the first person in the Table that would usually give me both an Id and a name but in the 
#print statement I am only selecting the name
#print(cur.fetchone())


#-----------------------------------OTHER--------------------------------------------

#Manual Open for Curosuor

#Using this curosur method allows you to execute sql statements
#Open
#cur = conn.cursor() 
#Open with extras module
#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


#Excuting old sql statements

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
#cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))
#cur.execute("SELECT * FROM student WHERE id = %s;", (1,))