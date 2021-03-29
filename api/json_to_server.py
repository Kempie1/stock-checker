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
            except ValueError and AttributeError:
                print('Decoding JSON has failed')
    
    def checking_if_ticker_exists(self):
        self.DB_HOST = os.environ['DB_HOST',
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
                    pe_ratio_ttm,
                    EPS_TTM,
                    Earnings_Date,
                    Volume,
                    Avg_Volume_3_Month,
                    Market_Cap,
                    Volatility,
                    Beta,
                    One_year_Target_Est,
                    Ex_Dividend_Date,
                    Total_Revenue,
                    Gross_Profit,
                    Profit_Margin,
                    Operating_Margin_ttm,
                    Revenue_Per_Share_ttm,
                    Quarterly_Revenue_Growth_yoy,
                    Gross_Profit_ttm,
                    Net_Income_Avi_to_Common_ttm,
                    Quarterly_Earnings_Growth_yoy,
                    Return_on_Assets_ttm,
                    Return_on_Equity_ttm,
                    Operating_Cash_Flow_ttm,
                    Fiscal_Year_Ends,
                    Most_Recent_Quarter_mrq,
                    Levered_Free_Cash_Flow_ttm,
                    Total_Cash_mrq,
                    Total_Cash_Per_Share_mrq,
                    Total_Debt_mrq,
                    Total_Debt_DIVIDED_Equity_mrq,
                    Current_Ratio_mrq,
                    Book_Value_Per_Share_mrq,
                    Beta_5Y_Monthly,
                    Fifty_Two_Week_Change,
                    averageVolume,
                    Fifty_Two_Week_High,
                    Fifty_Two_Week_Low,
                    Fifty_Day_Moving_Average,
                    Two_Hundred_Day_Moving_Average,
                    Avg_Vol_Ten_day,
                    Forward_Annual_Dividend_Rate,
                    Forward_Annual_Dividend_Yield,
                    Payout_Ratio,
                    Dividend_Date,
                    Trailing_Annual_Dividend_Rate,
                    Trailing_Annual_Dividend_Yield,
                    Five_Year_Average_Dividend_Yield,

                ) values  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                returning stock
                ''', (
                    validate(['symbol']),
                    validate(['quoteType','longName']),
                    validate(['price','regularMarketPrice'])['raw'],
                    validate(['summaryDetail','regularMarketPreviousClose']['raw'],
                    validate(['price','regularMarketOpen']['raw'],
                    validate(['summaryDetail','bid']['raw'],
                    validate(['summaryDetail','bidSize']['raw'],
                    validate(['summaryDetail','ask']['raw'],
                    validate(['summaryDetail','askSize']['raw'],
                    validate(['summaryDetail','dayHigh']['raw'],
                    validate(['summaryDetail','dayLow']['raw'],
                    validate(['summaryDetail','fiftyTwoWeekHigh']['raw'],
                    validate(['summaryDetail','fiftyTwoWeekLow']['raw'],
                    validate(['summaryDetail','trailingPE']['raw'],
                    validate(['defaultKeyStatistics','trailingEps']['raw'],
                    [validate(['calendarEvents','earnings','earningsDate','0']['raw'],
                    validate(['calendarEvents','earnings','earningsDate','1']['raw']],
                    validate(['summaryDetail','volume']['raw'],
                    validate(['price','averageDailyVolume3Month'])['raw'],
                    validate(['price','marketCap'])['raw'],
                    #TBeta_5Y_Monthly
                    validate(['defaultKeyStatistics','volatility']['raw'],
                    validate(['defaultKeyStatistics','beta']['raw'],
                    validate(['financialData','targetMeanPrice']['raw'],#
                    #Forward_Dividend_AND_Yield
                    validate(['summaryDetail','exDividendDate']['raw'],
                    #Basic_Average_Shares
                    #Diluted_Average_Shares
                    validate(['financialData','totalRevenue']['raw'],
                    #Other_Income_Expense
                    #Basic_EPS
                    #Diluted_EPS
                    #EBIT
                    #Total_Unusual_Items_Excluding_Goodwill
                    #Total_Unusual_Items
                    validate(['financialData','grossProfits']['raw'],
                    #Operating_Income
                    #Pretax_Income
                    #Net_Income_Common_Stockholders
                    #Diluted_NI_Available_to_Com_Stockholders
                    #Total_Operating_Income_as_Reported
                    #Net_Income_from_Continuing_AND_Discontinued_Operation
                    #Normalized_Income
                    #Net_Income_from_Continuing_Operation_Net_Minority_Interest
                    #Normalized_EBITDA
                    #Cost_of_Revenue
                    #Operating_Expense 
                    #Tax_Provision
                    #Total_Expenses 
                    #Reconciled_Cost_of_Revenue 
                    #Reconciled_Depreciation 
                    #Tax_Effect_of_Unusual_Items 
                    validate(['defaultKeyStatistics','profitMargin']['raw'],
                    validate(['financialData','operatingMargins']['raw'], 
                    #Revenue_ttm
                    validate(['financialData','revenuePerShare']['raw'], 
                    validate(['financialData','revenueGrowth']['raw'],
                    #Gross_Profit_ttm
                    validate(['financialData','ebitda']['raw'],
                    validate(['defaultKeyStatistics','netIncomeToCommon']['raw'],
                    #Diluted_EPS_ttm
                    validate(['defaultKeyStatistics','earningsQuarterlyGrowth']['raw'], 
                    validate(['financialData','returnOnAssets']['raw'],
                    validate(['financialData','returnOnEquity']['raw'],
                    validate(['financialData','operatingCashflow']['raw'],
                    validate(['financialData','freeCashflow']['raw'],  
                    validate(['defaultKeyStatistics','nextFiscalYearEnd']['raw'],
                    validate(['defaultKeyStatistics','mostRecentQuarter']['raw'],
                    validate(['financialData','totalCash']['raw'],
                    validate(['financialData','totalCashPerShare']['raw'],
                    validate(['financialData','totalDebt']['raw'],
                    validate(['financialData','debtToEquity']['raw'],
                    validate(['financialData','currentRatio']['raw'],
                    validate(['defaultKeyStatistics','bookValue']['raw'],
                    validate(['summaryDetail','beta']['raw'],
                    validate(['defaultKeyStatistics','52WeekChange']['raw'],
                    validate(['summaryDetail','averageVolume']['raw'],
                    validate(['summaryDetail','FiftyTwoWeekHigh']['raw'],
                    validate(['summaryDetail','FiftyTwoWeekLow']['raw'],
                    validate(['summaryDetail','FiftyDayAverage']['raw'],
                    validate(['summaryDetail','TwoHundredDayAverage']['raw'],
                    #Avg_Vol_3_month
                    validate(['summaryDetail','averageVolume10Day']['raw'],
                    #Shares_Outstanding 
                    #Float
                    #Percentage_Held_by_Insiders
                    #Percentage_Held_by_Institutions
                    #Shares_Short
                    #Short_Ratio
                    #Short_Percentage_of_Float
                    #Short_Percentage_of_Shares_Outstanding
                    #Shares_Short_Prior
                    validate(['summaryDetail','dividendRate']['raw'],
                    validate(['summaryDetail','dividendYield']['raw'],
                    validate(['summaryDetail','payoutRatio']['raw'],
                    validate(['calendarEvents','dividendDate']['raw'],
                    validate(['summaryDetail','trailingAnnualDividendRate']['raw'],
                    validate(['summaryDetail','trailingAnnualDividendYield']['raw'],
                    validate(['summaryDetail','fiveYearAvgDividendYield']['raw'],
                    #Last_Split_Factor
                    #Last_Split_Date
                    
                    #WITHOUT THE HASTAGES IT CONTAINS 59 LINES UNTIL HERE


                    #SKIP FINANCIALS
                    #OTHER INCOME EXPENSE
                    #BASIC EPS
                    #Diluted eps
                    #Ebit
                    #Totalunusual items goodwill
                    #Totalunusual items
                    #Cost of revenue
                    #Expense
                    #tax
                    #Expenses
                    #Reconsiled
                    #Reconsiled
                    #tax
                                        
                    validate(['defaultKeyStatistics','SandP52WeekChange']
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


                    