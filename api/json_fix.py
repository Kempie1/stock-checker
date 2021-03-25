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
                    
                    Ticker_symbol = "n/a"
                    Stock_name = "n/a"
                    Stock_price = "n/a"
                    Previous_close = "n/a"
                    Open = "n/a"
                    Bid = "n/a"
                    Bid_Size = "n/a"
                    Ask = "n/a"
                    Ask_Size = "n/a"
                    Days_Range_High = "n/a"
                    Days_Range_Low = "n/a"
                    Fifty_Two_Week_Range_High = "n/a"
                    Fifty_Two_Week_Range_Low = "n/a"
                    PE_Ratio_TTM = "n/a"
                    EPS_TTM = "n/a"
                    Earnings_Date =["n/a"],
                    Volume = "n/a"
                    Avg_Volume = "n/a"
                    Market_Cap = "n/a"
                    TBeta_5Y_Monthly = "n/a"
                    Volatility = "n/a"
                    Beta = "n/a"
                    One_year_Target_Est = "n/a"
                    Forward_Dividend_AND_Yield = "n/a"
                    Ex_Dividend_Date = "n/a"
                    Basic_Average_Shares = "n/a"
                    Diluted_Average_Shares = "n/a"
                    Total_Revenue = "n/a"
                    Other_Income_Expense = "n/a"
                    Basic_EPS = "n/a"
                    Diluted_EPS = "n/a"
                    EBIT = "n/a"
                    Total_Unusual_Items_Excluding_Goodwill = "n/a"
                    Total_Unusual_Items = "n/a"
                    Gross_Profit = "n/a"
                    Operating_Income = "n/a"
                    Pretax_Income = "n/a"
                    Net_Income_Common_Stockholders = "n/a"
                    Diluted_NI_Available_to_Com_Stockholders = "n/a"
                    Total_Operating_Income_as_Reported = "n/a"
                    Net_Income_from_Continuing_AND_Discontinued_Operation = "n/a"
                    Normalized_Income = "n/a"
                    Net_Income_from_Continuing_Operation_Net_Minority_Interest = "n/a"
                    Normalized_EBITDA = "n/a"
                    Cost_of_Revenue = "n/a"
                    Operating_Expense = "n/a"
                    Tax_Provision = "n/a"
                    Total_Expenses = "n/a"
                    Reconciled_Cost_of_Revenue = "n/a"
                    Reconciled_Depreciation = "n/a"
                    Tax_Effect_of_Unusual_Items = "n/a"
                    Profit_Margin = "n/a"
                    Operating_Margin_ttm = "n/a"
                    Revenue_ttm = "n/a"
                    Revenue_Per_Share_ttm = "n/a"
                    Quarterly_Revenue_Growth_yoy = "n/a"
                    Gross_Profit_ttm = "n/a"
                    EBITDA = "n/a"
                    Net_Income_Avi_to_Common_ttm = "n/a"
                    Diluted_EPS_ttm = "n/a"
                    Quarterly_Earnings_Growth_yoy = "n/a"
                    Return_on_Assets_ttm = "n/a"
                    Return_on_Equity_ttm = "n/a"
                    Operating_Cash_Flow_ttm = "n/a"
                    Levered_Free_Cash_Flow_ttm = "n/a"
                    Fiscal_Year_Ends = "n/a"
                    Most_Recent_Quarter_mrq = "n/a"
                    Total_Cash_mrq = "n/a"
                    Total_Cash_Per_Share_mrq = "n/a"
                    Total_Debt_mrq = "n/a"
                    Total_Debt_DIVIDED_Equity_mrq = "n/a"
                    Current_Ratio_mrq = "n/a"
                    Book_Value_Per_Share_mrq = "n/a"
                    Beta_5Y_Monthly = "n/a"
                    Fifty_Two_Week_Change = "n/a"
                    averageVolume = "n/a"
                    Fifty_Two_Week_High = "n/a"
                    Fifty_Two_Week_Low = "n/a"
                    Fifty_Day_Moving_Average = "n/a"
                    Two_Hundred_Day_Moving_Average = "n/a"
                    Avg_Vol_3_month = "n/a"
                    Avg_Vol_Ten_day = "n/a"
                    Shares_Outstanding = "n/a"
                    Float = "n/a"
                    Percentage_Held_by_Insiders = "n/a"
                    Percentage_Held_by_Institutions = "n/a"
                    Shares_Short = "n/a"
                    Short_Ratio = "n/a"
                    Short_Percentage_of_Float = "n/a"
                    Short_Percentage_of_Shares_Outstanding = "n/a"
                    Shares_Short_Prior = "n/a"
                    Forward_Annual_Dividend_Rate = "n/a"
                    Forward_Annual_Dividend_Yield = "n/a"
                    Trailing_Annual_Dividend_Rate = "n/a"
                    Trailing_Annual_Dividend_Yield = "n/a"
                    Five_Year_Average_Dividend_Yield = "n/a"
                    Payout_Ratio = "n/a"
                    Dividend_Date = "n/a"
                    Last_Split_Factor = "n/a"
                    Last_Split_Date = "n/a"

                    try:
                        Ticker_symbol = self.data['symbol']
                    except KeyError:

                    try:
                        Stock_name = self.data['quoteType']['longName']
                    except KeyError:

                    try:
                        Stock_price =  
                    except KeyError:

                    try:
                        Previous_close =  
                    except KeyError:

                    try:
                        Open =  
                    except KeyError:

                    try:
                        Bid =  
                    except KeyError:

                    try:
                        Bid_Size =  
                    except KeyError:

                    try:
                        Ask =  
                    except KeyError:

                    try:
                        Ask_Size =  
                    except KeyError:

                    try:
                        Days_Range_High =  
                    except KeyError:

                    try:
                        Days_Range_Low =  
                    except KeyError:

                    try:
                        Fifty_Two_Week_Range_High =  
                    except KeyError:

                    try:
                        Fifty_Two_Week_Range_Low =  
                    except KeyError:

                    try:
                        PE_Ratio_TTM =  
                    except KeyError:

                    try:
                        EPS_TTM =  
                    except KeyError:

                    try:
                        Earnings_Date =
                    except KeyError:

                    try:
                        Volume =  
                    except KeyError:

                    try:
                        Avg_Volume =  
                    except KeyError:

                    try:
                        Market_Cap =  
                    except KeyError:

                    try:
                        TBeta_5Y_Monthly =  
                    except KeyError:

                    try:
                        Volatility =  
                    except KeyError:

                    try:
                        Beta =  
                    except KeyError:

                    try:
                        One_year_Target_Est =  
                    except KeyError:

                    try:
                        Forward_Dividend_AND_Yield =  
                    except KeyError:

                    try:
                        Ex_Dividend_Date =  
                    except KeyError:

                    try:
                        Basic_Average_Shares =  
                    except KeyError:

                    try:
                        Diluted_Average_Shares =  
                    except KeyError:

                    try:
                        Total_Revenue =  
                    except KeyError:

                    try:
                        Other_Income_Expense =  
                    except KeyError:

                    try:
                        Basic_EPS =  
                    except KeyError:

                    try:
                        Diluted_EPS =  
                    except KeyError:

                    try:
                        EBIT =  
                    except KeyError:

                    try:
                        Total_Unusual_Items_Excluding_Goodwill =  
                    except KeyError:

                    try:
                        Total_Unusual_Items =  
                    except KeyError:

                    try:
                        Gross_Profit =  
                    except KeyError:

                    try:
                        Operating_Income =  
                    except KeyError:

                    try:
                        Pretax_Income =  
                    except KeyError:

                    try:
                        Net_Income_Common_Stockholders =  
                    except KeyError:

                    try:
                        Diluted_NI_Available_to_Com_Stockholders =  
                    except KeyError:

                    try:
                        Total_Operating_Income_as_Reported =  
                    except KeyError:

                    try:
                        Net_Income_from_Continuing_AND_Discontinued_Operation =  
                    except KeyError:

                    try:
                        Normalized_Income =  
                    except KeyError:

                    try:
                        Net_Income_from_Continuing_Operation_Net_Minority_Interest =  
                    except KeyError:

                    try:
                        Normalized_EBITDA =  
                    except KeyError:

                    try:
                        Cost_of_Revenue =  
                    except KeyError:

                    try:
                        Operating_Expense =  
                    except KeyError:

                    try:
                        Tax_Provision =  
                    except KeyError:

                    try:
                        Total_Expenses =  
                    except KeyError:

                    try:
                        Reconciled_Cost_of_Revenue =  
                    except KeyError:

                    try:
                        Reconciled_Depreciation =  
                    except KeyError:

                    try:
                        Tax_Effect_of_Unusual_Items =  
                    except KeyError:

                    try:
                        Profit_Margin =  
                    except KeyError:

                    try:
                        Operating_Margin_ttm =  
                    except KeyError:

                    try:
                        Revenue_ttm =  
                    except KeyError:

                    try:
                        Revenue_Per_Share_ttm =  
                    except KeyError:

                    try:
                        Quarterly_Revenue_Growth_yoy =  
                    except KeyError:

                    try:
                        Gross_Profit_ttm =  
                    except KeyError:

                    try:
                        EBITDA =  
                    except KeyError:

                    try:
                        Net_Income_Avi_to_Common_ttm =  
                    except KeyError:

                    try:
                        Diluted_EPS_ttm =  
                    except KeyError:

                    try:
                        Quarterly_Earnings_Growth_yoy =  
                    except KeyError:

                    try:
                        Return_on_Assets_ttm =  
                    except KeyError:

                    try:
                        Return_on_Equity_ttm =  
                    except KeyError:

                    try:
                        Operating_Cash_Flow_ttm =  
                    except KeyError:

                    try:
                        Levered_Free_Cash_Flow_ttm =  
                    except KeyError:

                    try:
                        Fiscal_Year_Ends =  
                    except KeyError:

                    try:
                        Most_Recent_Quarter_mrq =  
                    except KeyError:

                    try:
                        Total_Cash_mrq =  
                    except KeyError:

                    try:
                        Total_Cash_Per_Share_mrq =  
                    except KeyError:

                    try:
                        Total_Debt_mrq =  
                    except KeyError:

                    try:
                        Total_Debt_DIVIDED_Equity_mrq =  
                    except KeyError:

                    try:
                        Current_Ratio_mrq =  
                    except KeyError:

                    try:
                        Book_Value_Per_Share_mrq =  
                    except KeyError:

                    try:
                        Beta_5Y_Monthly =  
                    except KeyError:

                    try:
                        Fifty_Two_Week_Change =  
                    except KeyError:

                    try:
                        averageVolume =  
                    except KeyError:

                    try:
                        Fifty_Two_Week_High =  
                    except KeyError:

                    try:
                        Fifty_Two_Week_Low =  
                    except KeyError:

                    try:
                        Fifty_Day_Moving_Average =  
                    except KeyError:

                    try:
                        Two_Hundred_Day_Moving_Average =  
                    except KeyError:

                    try:
                        Avg_Vol_3_month =  
                    except KeyError:

                    try:
                        Avg_Vol_Ten_day =  
                    except KeyError:

                    try:
                        Shares_Outstanding =  
                    except KeyError:

                    try:
                        Float =  
                    except KeyError:

                    try:
                        Percentage_Held_by_Insiders =  
                    except KeyError:

                    try:
                        Percentage_Held_by_Institutions =  
                    except KeyError:

                    try:
                        Shares_Short =  
                    except KeyError:

                    try:
                        Short_Ratio =  
                    except KeyError:

                    try:
                        Short_Percentage_of_Float =  
                    except KeyError:

                    try:
                        Short_Percentage_of_Shares_Outstanding =  
                    except KeyError:

                    try:
                        Shares_Short_Prior =  
                    except KeyError:

                    try:
                        Forward_Annual_Dividend_Rate =  
                    except KeyError:

                    try:
                        Forward_Annual_Dividend_Yield =  
                    except KeyError:

                    try:
                        Trailing_Annual_Dividend_Rate =  
                    except KeyError:

                    try:
                        Trailing_Annual_Dividend_Yield =  
                    except KeyError:

                    try:
                        Five_Year_Average_Dividend_Yield =  
                    except KeyError:

                    try:
                        Payout_Ratio =  
                    except KeyError:

                    try:
                        Dividend_Date =  
                    except KeyError:

                    try:
                        Last_Split_Factor = ""
                    except KeyError:

                    try:
                        Last_Split_Date =  ""
                    except KeyError:




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
                    Ticker_symbol,
                    Stock_name,
                    Stock_price,
                    Previous_close,
                    Open,
                    Bid,
                    Bid_Size,
                    Ask,
                    Ask_Size,
                    Days_Range_High,
                    Days_Range_Low,
                    Fifty_Two_Week_Range_High,
                    Fifty_Two_Week_Range_Low,
                    PE_Ratio_TTM,
                    EPS_TTM,
                    Earnings_Date =["n/a"],
                    Volume,
                    Avg_Volume,
                    Market_Cap,
                    TBeta_5Y_Monthly,
                    Volatility,
                    Beta,
                    One_year_Target_Est,
                    Forward_Dividend_AND_Yield,
                    Ex_Dividend_Date,
                    Basic_Average_Shares,
                    Diluted_Average_Shares,
                    Total_Revenue,
                    Other_Income_Expense,
                    Basic_EPS,
                    Diluted_EPS,
                    EBIT,
                    Total_Unusual_Items_Excluding_Goodwill,
                    Total_Unusual_Items,
                    Gross_Profit,
                    Operating_Income,
                    Pretax_Income,
                    Net_Income_Common_Stockholders,
                    Diluted_NI_Available_to_Com_Stockholders,
                    Total_Operating_Income_as_Reported,
                    Net_Income_from_Continuing_AND_Discontinued_Operation,
                    Normalized_Income,
                    Net_Income_from_Continuing_Operation_Net_Minority_Interest,
                    Normalized_EBITDA,
                    Cost_of_Revenue,
                    Operating_Expense,
                    Tax_Provision,
                    Total_Expenses,
                    Reconciled_Cost_of_Revenue,
                    Reconciled_Depreciation,
                    Tax_Effect_of_Unusual_Items,
                    Profit_Margin,
                    Operating_Margin_ttm,
                    Revenue_ttm,
                    Revenue_Per_Share_ttm,
                    Quarterly_Revenue_Growth_yoy,
                    Gross_Profit_ttm,
                    EBITDA,
                    Net_Income_Avi_to_Common_ttm,
                    Diluted_EPS_ttm,
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
                    Avg_Vol_3_month,
                    Avg_Vol_Ten_day,
                    Shares_Outstanding,
                    Float,
                    Percentage_Held_by_Insiders,
                    Percentage_Held_by_Institutions,
                    Shares_Short,
                    Short_Ratio,
                    Short_Percentage_of_Float,
                    Short_Percentage_of_Shares_Outstanding,
                    Shares_Short_Prior,
                    Forward_Annual_Dividend_Rate,
                    Forward_Annual_Dividend_Yield,
                    Trailing_Annual_Dividend_Rate,
                    Trailing_Annual_Dividend_Yield,
                    Five_Year_Average_Dividend_Yield,
                    Payout_Ratio,
                    Dividend_Date,
                    Last_Split_Factor,
                    Last_Split_Date,
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

