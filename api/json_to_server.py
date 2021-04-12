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
        self.DB_HOST = os.environ['DB_HOST']
        self.DB_NAME = os.environ['DB_NAME']
        self.DB_USER = os.environ['DB_USER']
        self.DB_PASS = os.environ['DB_PASS']

        conn = psycopg2.connect(dbname = self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)

        with conn: 
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT stock.ticker_symbol FROM stock")
                    self.ticker_table = cur.fetchall()

        json_ticker_symbol = self.data['get-statistics']['symbol']
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
        
        def validate_api(l):
            cursor=self.data
            for x in range(len(l)):
                if x==(len(l)-1):
                    if l[x] in cursor:
                        cursor=cursor.get(l[x])
                        if 'raw' in cursor:
                            return cursor.get('raw')
                        if not cursor:
                            return "n/a"
                        if isinstance(cursor, list):
                            if 'raw' in cursor[0]:
                                return cursor[0].get('raw')
                        return cursor
                    else:
                        return "n/a"
                else:
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
                    Beta,
                    One_year_Target_Est,
                    Ex_Dividend_Date,
                    Total_Revenue,
                    Gross_Profit,
                    Profit_Margin,
                    Operating_Margin_ttm,
                    Revenue_Per_Share_ttm,
                    Quarterly_Revenue_Growth_yoy,
                    EBITDA,
                    Net_Income_Avi_to_Common_ttm,
                    Quarterly_Earnings_Growth_yoy,
                    Return_on_Assets_ttm,
                    Return_on_Equity_ttm,
                    Operating_Cash_Flow_ttm,
                    Levered_Free_Cash_Flow_ttm,
                    Fiscal_Year_Ends,
                    Most_Recent_Quarter_mrq,
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
                    Five_Year_Average_Dividend_Yield
                ) values  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                returning stock
                ''', (
                    validate_api(['get-statistics','symbol']),
                    validate_api(['get-statistics','quoteType','longName']),
                    validate_api(['get-statistics','price','regularMarketPrice']),
                    validate_api(['get-statistics','summaryDetail','regularMarketPreviousClose']),
                    validate_api(['get-statistics','price','regularMarketOpen']),
                    validate_api(['get-statistics','summaryDetail','bid']),
                    validate_api(['get-statistics','summaryDetail','bidSize']),
                    validate_api(['get-statistics','summaryDetail','ask']),
                    validate_api(['get-statistics','summaryDetail','askSize']),
                    validate_api(['get-statistics','summaryDetail','dayHigh']),
                    validate_api(['get-statistics','summaryDetail','dayLow']),
                    validate_api(['get-statistics','summaryDetail','fiftyTwoWeekHigh']),
                    validate_api(['get-statistics','summaryDetail','fiftyTwoWeekLow']),
                    validate_api(['get-statistics','summaryDetail','trailingPE']),
                    validate_api(['get-statistics','defaultKeyStatistics','trailingEps']),
                    validate_api(['get-statistics','calendarEvents','earnings','earningsDate']),
                    validate_api(['get-statistics','summaryDetail','volume']),
                    validate_api(['get-statistics','get-statistics','price','averageDailyVolume3Month']),
                    validate_api(['get-statistics','price','marketCap']),
                    #TBeta_5Y_Monthly
                    #volatility
                    validate_api(['get-statistics','defaultKeyStatistics','beta']),
                    validate_api(['get-statistics','financialData','targetMeanPrice']),
                    #Forward_Dividend_AND_Yield
                    validate_api(['get-statistics','summaryDetail','exDividendDate']),
                    #Basic_Average_Shares
                    #Diluted_Average_Shares
                    validate_api(['get-statistics','financialData','totalRevenue']),
                    #Other_Income_Expense
                    #Basic_EPS
                    #Diluted_EPS
                    #EBIT
                    #Total_Unusual_Items_Excluding_Goodwill
                    #Total_Unusual_Items
                    validate_api(['get-statistics','financialData','grossProfits']),
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
                    validate_api(['get-statistics','defaultKeyStatistics','profitMargin']),
                    validate_api(['get-statistics','financialData','operatingMargins']), 
                    #Revenue_ttm
                    validate_api(['get-statistics','financialData','revenuePerShare']), 
                    validate_api(['get-statistics','financialData','revenueGrowth']),
                    #Gross_Profit_ttm
                    validate_api(['get-statistics','financialData','ebitda']),
                    validate_api(['get-statistics','defaultKeyStatistics','netIncomeToCommon']),
                    #Diluted_EPS_ttm
                    validate_api(['get-statistics','defaultKeyStatistics','earningsQuarterlyGrowth']), 
                    validate_api(['get-statistics','financialData','returnOnAssets']),
                    validate_api(['get-statistics','financialData','returnOnEquity']),
                    validate_api(['get-statistics','financialData','operatingCashflow']),
                    validate_api(['get-statistics','financialData','freeCashflow']),  
                    validate_api(['get-statistics','defaultKeyStatistics','nextFiscalYearEnd']),
                    validate_api(['get-statistics','defaultKeyStatistics','mostRecentQuarter']),
                    validate_api(['get-statistics','financialData','totalCash']),
                    validate_api(['get-statistics','financialData','totalCashPerShare']),
                    validate_api(['get-statistics','financialData','totalDebt']),
                    validate_api(['get-statistics','financialData','debtToEquity']),
                    validate_api(['get-statistics','financialData','currentRatio']),
                    validate_api(['get-statistics','defaultKeyStatistics','bookValue']),
                    validate_api(['get-statistics','summaryDetail','beta']),
                    validate_api(['get-statistics','defaultKeyStatistics','52WeekChange']),
                    validate_api(['get-statistics','summaryDetail','averageVolume']),
                    validate_api(['get-statistics','summaryDetail','FiftyTwoWeekHigh']),
                    validate_api(['get-statistics','summaryDetail','FiftyTwoWeekLow']),
                    validate_api(['get-statistics','summaryDetail','FiftyDayAverage']),
                    validate_api(['get-statistics','summaryDetail','TwoHundredDayAverage']),
                    #Avg_Vol_3_month
                    validate_api(['get-statistics','summaryDetail','averageVolume10Day']),
                    #Shares_Outstanding 
                    #Float
                    #Percentage_Held_by_Insiders
                    #Percentage_Held_by_Institutions
                    #Shares_Short
                    #Short_Ratio
                    #Short_Percentage_of_Float
                    #Short_Percentage_of_Shares_Outstanding
                    #Shares_Short_Prior
                    validate_api(['get-statistics','summaryDetail','dividendRate']),
                    validate_api(['get-statistics','summaryDetail','dividendYield']),
                    validate_api(['get-statistics','summaryDetail','payoutRatio']),
                    validate_api(['get-statistics','calendarEvents','dividendDate']),
                    validate_api(['get-statistics','summaryDetail','trailingAnnualDividendRate']),
                    validate_api(['get-statistics','summaryDetail','trailingAnnualDividendYield']),
                    validate_api(['get-statistics','summaryDetail','fiveYearAvgDividendYield'])
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


                    