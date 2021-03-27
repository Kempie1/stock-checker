import psycopg2
import psycopg2.extras
import json
import requests
from json.decoder import JSONDecodeError
import os

class Json_to_server():
    def open_json_file(self):
        with open('stock.json') as json_file:
            try:
                self.data = json.load(json_file)
            except ValueError:
                print('Decoding JSON has failed')
    
    def checking_if_ticker_exists(self):
        self.DB_HOST = os.environ['DB_HOST']
        self.DB_NAME = os.environ['DB_NAME']
        self.DB_USER = os.environ['DB_USER']
        self.DB_PASS = os.environ['DB_PASS']

        conn = psycopg2.connect(dbname = self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)

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

        if len(self.ticker_table) == 0:
            print("There is nothing in the ticker_symbol Table")
            self.already_exists_in_DB = False

    #Receives the address as a list, then checks if the exist, returns a dictionary object or value if there is no 'raw'
    

    def connecting_to_server(self):
        
        def validate_api(l):
            cursor=self.data
            for x in range(len(l)):
                if x==(len(l)-1):
                    if l[x] in cursor:
                        return cursor.get(l[x])
                if l[x] in cursor:
                    cursor=cursor.get(l[x])
                else:
                    return "n/a"

        conn = psycopg2.connect(dbname = self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)
        if self.already_exists_in_DB == False:
            with conn: 
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT stock.ticker_symbol FROM stock")
                    self.ticker_table = cur.fetchall()

                    cur.execute('''
                INSERT INTO stock (
                    ticker_symbol,
                    stock_name
                ) values  (%s,%s)
                returning stock
                ''', (
                    validate_api(['symbol']),
                    validate_api(['quoteType','longName'])
                   # self.data['price']['regularMarketPrice']['raw']
                    #self.data['summaryDetail']['regularMarketPreviousClose']['raw'],
                    #self.data['price']['regularMarketOpen']['raw'],
                   # self.data['summaryDetail']['bid']['raw'],
                   # self.data['summaryDetail']['bidSize']['raw'],
                   # self.data['summaryDetail']['ask']['raw'],
                   # self.data['summaryDetail']['askSize']['raw'],#9
                   # self.data['summaryDetail']['dayHigh']['raw'],
                   # self.data['summaryDetail']['dayLow']['raw'],
                   # self.data['summaryDetail']['fiftyTwoWeekHigh']['raw'],
                   # self.data['summaryDetail']['fiftyTwoWeekLow']['raw'],
                    #self.data['summaryDetail']['trailingPE']['raw'],#
                    #self.data['defaultKeyStatistics']['trailingEps']['raw'],
                    #[self.data['calendarEvents']['earnings']['earningsDate']['0']['fmt'],
                    #self.data['calendarEvents']['earnings']['earningsDate']['1']['fmt']],
                )
            )

                    print(cur.fetchall())
                    print("Everything was added to the database")

            conn.commit()
            conn.close()

        
                    

server = Json_to_server()
server.open_json_file()
server.checking_if_ticker_exists()
#server.validate()
server.connecting_to_server()


                    #previous_close,
                    #open,
                    #bid,
                    #bid_size,
                    #ask,
                    #ask_size,
                    #Days_Range_High,
                    #Days_Range_Low,
                    #Fifty_Two_Week_Range_High,
                    #Fifty_Two_Week_Range_Low