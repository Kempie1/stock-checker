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
        DB_HOST = "ec2-54-247-158-179.eu-west-1.compute.amazonaws.com"
        DB_NAME = "d9k5l1lp51eomr"
        DB_USER = "dxotskvadresqz" 
        DB_PASS = "0b9cd2ee889fc10b9503feb819cbcf02c95a46d29e0bdf86507e3db4d14f2b99"

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

        if len(self.ticker_table) == 0:
            print("There is nothing in the ticker_symbol Table")
            self.already_exists_in_DB = False

    def connecting_to_server(self):
        
        DB_HOST = "ec2-54-247-158-179.eu-west-1.compute.amazonaws.com"
        DB_NAME = "d9k5l1lp51eomr"
        DB_USER = "dxotskvadresqz" 
        DB_PASS = "0b9cd2ee889fc10b9503feb819cbcf02c95a46d29e0bdf86507e3db4d14f2b99"

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
                    open,
                    bid,
                    bid_size,
                    ask,
                    ask_size,
                    Days_Range_High,
                    Days_Range_Low,
                    Fifty_Two_Week_Range_High,
                    Fifty_Two_Week_Range_Low,
                    EPS_TTM,
                    Earnings_Date
                ) values  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                returning stock
                ''', (
                    self.data['symbol'],
                    self.data['quoteType']['longName'],
                    self.data['price']['regularMarketPrice']['raw'],
                    self.data['summaryDetail']['regularMarketPreviousClose']['raw'],
                    self.data['price']['regularMarketOpen']['raw'],
                    self.data['summaryDetail']['bid']['raw'],
                    self.data['summaryDetail']['bidSize']['raw'],
                    self.data['summaryDetail']['ask']['raw'],
                    self.data['summaryDetail']['askSize']['raw'],#9
                    self.data['summaryDetail']['dayHigh']['raw'],
                    self.data['summaryDetail']['dayLow']['raw'],
                    self.data['summaryDetail']['fiftyTwoWeekHigh']['raw'],
                    self.data['summaryDetail']['fiftyTwoWeekLow']['raw'],
                    #self.data['summaryDetail']['trailingPE']['raw'],#
                    self.data['defaultKeyStatistics']['trailingEps']['raw'],
                    [self.data['calendarEvents']['earnings']['earningsDate']['0']['fmt'],
                    self.data['calendarEvents']['earnings']['earningsDate']['1']['fmt']],
                )
            )

                    print(cur.fetchall())
                    print("Everything was added to the database")

                conn.commit()
                conn.close()
        
                    

server = Json_to_server()
#server.open_json_file()
#server.checking_if_ticker_exists()
#server.connecting_to_server()

