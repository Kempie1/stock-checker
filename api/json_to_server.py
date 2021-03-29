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
                    validate_api(['symbol']),
                    validate_api(['quoteType','longName']),
                    validate_api(['price','regularMarketPrice','raw']),
                    validate_api(['summaryDetail','regularMarketPreviousClose','raw']),
                    validate_api(['price','regularMarketOpen','raw']),
                    validate_api(['summaryDetail','bid','raw']),
                    validate_api(['summaryDetail','bidSize','raw']),
                    validate_api(['summaryDetail','ask','raw']),
                    validate_api(['summaryDetail','askSize','raw']),
                    validate_api(['summaryDetail','dayHigh','raw']),
                    validate_api(['summaryDetail','dayLow','raw']),
                    validate_api(['summaryDetail','fiftyTwoWeekHigh','raw']),
                    validate_api(['summaryDetail','fiftyTwoWeekLow','raw']),
                    validate_api(['summaryDetail','trailingPE','raw']),
                    validate_api(['defaultKeyStatistics','trailingEps','raw']),
                    validate_api(['calendarEvents','earnings','earningsDate','0','raw']),
                    validate_api(['calendarEvents','earnings','earningsDate','1','raw']),
                    validate_api(['summaryDetail','volume','raw']),
                    validate_api(['price','averageDailyVolume3Month','raw']),
                    validate_api(['price','marketCap','raw']),
                    #TBeta_5Y_Monthly
                    validate_api(['defaultKeyStatistics','volatility','raw']),
                    validate_api(['defaultKeyStatistics','beta','raw']),
                    validate_api(['financialData','targetMeanPrice','raw']),
                    #Forward_Dividend_AND_Yield
                    validate_api(['summaryDetail','exDividendDate','raw']),
                    #Basic_Average_Shares
                    #Diluted_Average_Shares
                    validate_api(['financialData','totalRevenue','raw']),
                    #Other_Income_Expense
                    #Basic_EPS
                    #Diluted_EPS
                    #EBIT
                    #Total_Unusual_Items_Excluding_Goodwill
                    #Total_Unusual_Items
                    validate_api(['financialData','grossProfits','raw']),
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
                    validate_api(['defaultKeyStatistics','profitMargin','raw']),
                    validate_api(['financialData','operatingMargins','raw']), 
                    #Revenue_ttm
                    validate_api(['financialData','revenuePerShare','raw']), 
                    validate_api(['financialData','revenueGrowth','raw']),
                    #Gross_Profit_ttm
                    validate_api(['financialData','ebitda','raw']),
                    validate_api(['defaultKeyStatistics','netIncomeToCommon','raw']),
                    #Diluted_EPS_ttm
                    validate_api(['defaultKeyStatistics','earningsQuarterlyGrowth','raw']), 
                    validate_api(['financialData','returnOnAssets','raw']),
                    validate_api(['financialData','returnOnEquity','raw']),
                    validate_api(['financialData','operatingCashflow','raw']),
                    validate_api(['financialData','freeCashflow','raw']),  
                    validate_api(['defaultKeyStatistics','nextFiscalYearEnd','raw']),
                    validate_api(['defaultKeyStatistics','mostRecentQuarter','raw']),
                    validate_api(['financialData','totalCash','raw']),
                    validate_api(['financialData','totalCashPerShare','raw']),
                    validate_api(['financialData','totalDebt','raw']),
                    validate_api(['financialData','debtToEquity','raw']),
                    validate_api(['financialData','currentRatio','raw']),
                    validate_api(['defaultKeyStatistics','bookValue','raw']),
                    validate_api(['summaryDetail','beta','raw']),
                    validate_api(['defaultKeyStatistics','52WeekChange','raw']),
                    validate_api(['summaryDetail','averageVolume','raw']),
                    validate_api(['summaryDetail','FiftyTwoWeekHigh','raw']),
                    validate_api(['summaryDetail','FiftyTwoWeekLow','raw']),
                    validate_api(['summaryDetail','FiftyDayAverage','raw']),
                    validate_api(['summaryDetail','TwoHundredDayAverage','raw']),
                    #Avg_Vol_3_month
                    validate_api(['summaryDetail','averageVolume10Day','raw']),
                    #Shares_Outstanding 
                    #Float
                    #Percentage_Held_by_Insiders
                    #Percentage_Held_by_Institutions
                    #Shares_Short
                    #Short_Ratio
                    #Short_Percentage_of_Float
                    #Short_Percentage_of_Shares_Outstanding
                    #Shares_Short_Prior
                    validate_api(['summaryDetail','dividendRate','raw']),
                    validate_api(['summaryDetail','dividendYield','raw']),
                    validate_api(['summaryDetail','payoutRatio','raw']),
                    validate_api(['calendarEvents','dividendDate','raw']),
                    validate_api(['summaryDetail','trailingAnnualDividendRate','raw']),
                    validate_api(['summaryDetail','trailingAnnualDividendYield','raw']),
                    validate_api(['summaryDetail','fiveYearAvgDividendYield','raw'])
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
                                        
                    #validate_api(['defaultKeyStatistics','SandP52WeekChange']
                )
            )

                    print(cur.fetchall())
                    print("Everything was added to the database")

            conn.commit()
            conn.close()

        
                    

server = Json_to_server()
server.open_json_file()
server.checking_if_ticker_exists()
#server.validate_api()
server.connecting_to_server()


                    