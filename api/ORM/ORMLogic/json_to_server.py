import psycopg2
import psycopg2.extras
import json
import requests
from json.decoder import JSONDecodeError
import os
from decouple import config
from ORM_services import ORM_services
from api_call_to_json import Api_call
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarative import Stock, Base
from datetime import datetime

class Json_to_server():
    
    def __init__(self):
        self.engine = create_engine(config("DB_URL"))
        self.services = ORM_services()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        

    
    def open_json_file(self, json_file):
        if os.path.getsize(json_file)>40:
            json_data = open(json_file,"r")
            self.data = json.load(json_data)
            return self.data
        return {}

        

    def checking_if_ticker_exists_in_database(self, ticker_symbol):
        self.already_exists_in_DB = self.services.checking_if_ticker_exists(ticker_symbol, ['REALCASE'])

    def send_data_to_server(self):
        
        def validate_api(l):
            cursor=self.data
            for x in range(len(l)):
                if x==(len(l)-1):
                    if l[x] in cursor:
                        cursor=cursor.get(l[x])
                        if 'raw' in cursor:
                            return cursor.get('raw')
                        if not cursor:
                            return None
                        if isinstance(cursor, list):
                            if 'raw' in cursor[0]:
                                return cursor[0].get('raw')
                        return cursor
                    else:
                        return None
                else:
                    if l[x] in cursor:
                        cursor=cursor.get(l[x])
                    else:
                        return None


        def toDate(i):
            if i is None:
                return None
            return datetime.utcfromtimestamp(i).strftime('%Y-%m-%d')
        self.session = self.DBSession()

        new_stock=Stock( \
        ticker_symbol                                               =validate_api(['get-statistics','symbol']),  \
        stock_name                                                  =validate_api(['get-statistics','quoteType','longName']),  \
        stock_price                                                 =validate_api(['get-statistics','price','regularMarketPrice']),  \
        previous_close                                              =validate_api(['get-statistics','summaryDetail','regularMarketPreviousClose']),  \
        open_bid                                                    =validate_api(['get-statistics','price','regularMarketOpen']),  \
        bid                                                         =validate_api(['get-statistics','summaryDetail','bid']),  \
        bid_size                                                    =validate_api(['get-statistics','summaryDetail','bidSize']),  \
        ask                                                         =validate_api(['get-statistics','summaryDetail','ask']),  \
        ask_size                                                    =validate_api(['get-statistics','summaryDetail','askSize']),  \
        days_range_high                                             =validate_api(['get-statistics','summaryDetail','dayHigh']),  \
        days_range_low                                              =validate_api(['get-statistics','summaryDetail','dayLow']),  \
        fifty_two_week_range_high                                   =validate_api(['get-statistics','summaryDetail','fiftyTwoWeekHigh']),  \
        fifty_two_week_range_low                                    =validate_api(['get-statistics','summaryDetail','fiftyTwoWeekLow']),  \
        pe_ratio_ttm                                                =validate_api(['get-statistics','summaryDetail','trailingPE']),  \
        eps_ttm                                                     =validate_api(['get-statistics','defaultKeyStatistics','trailingEps']),  \
        earnings_date                                               =toDate(validate_api(['get-statistics','calendarEvents','earnings','earningsDate'])),   \
        volume                                                      =validate_api(['get-statistics','summaryDetail','volume']),  \
        avg_volume_3_month                                          =validate_api(['get-statistics','get-statistics','price','averageDailyVolume3Month']),  \
        market_cap                                                  =validate_api(['get-statistics','price','marketCap']),  \
        #tbeta_5y_monthly                                            =#TBeta_5Y_Monthly  \
        #volatility                                                  =#volatility  \
        beta                                                        =validate_api(['get-statistics','defaultKeyStatistics','beta']),  \
        one_year_target_est                                         =validate_api(['get-statistics','financialData','targetMeanPrice']),  \
        #forward_dividend_and_yield                                  =#Forward_Dividend_AND_Yield  \
        ex_dividend_date                                            =toDate(validate_api(['get-statistics','summaryDetail','exDividendDate'])),  \
        
        #basic_average_shares                                        =#Basic_Average_Shares  \
        #diluted_average_shares                                      =#Diluted_Average_Shares  \
        total_revenue                                               =validate_api(['get-statistics','financialData','totalRevenue']),  \
        #other_income_expense                                        =#Other_Income_Expense  \
        #basic_eps                                                   =#Basic_EPS  \
        #diluted_eps                                                 =#Diluted_EPS  \
        #ebit                                                        =#EBIT  \
        #total_unusual_items_excluding_goodwill                      =#Total_Unusual_Items_Excluding_Goodwill  \
        #total_unusual_items                                         =#Total_Unusual_Items  \
        gross_profit                                                =validate_api(['get-statistics','financialData','grossProfits']),  \
        #operating_income                                            =#Operating_Income  \
        #pretax_income                                               =#Pretax_Income  \
        #net_income_common_stockholders                              =#Net_Income_Common_Stockholders  \
        #diluted_ni_available_to_com_stockholders                    =#Diluted_NI_Available_to_Com_Stockholders  \
        #total_operating_income_as_reported                          =#Total_Operating_Income_as_Reported  \
        #net_income_from_continuing_and_discontinued_operation       =#Net_Income_from_Continuing_AND_Discontinued_Operation  \
        #normalized_income                                           =#Normalized_Income  \
        #net_income_from_continuing_operation_net_minority_interest  =#Net_Income_from_Continuing_Operation_Net_Minority_Interest  \
        #normalized_ebitda                                           =#Normalized_EBITDA  \
        #cost_of_revenue                                             =#Cost_of_Revenue  \
        #operating_expense                                           =#Operating_Expense   \
        #tax_provision                                               =#Tax_Provision  \
        #total_expenses                                              =#Total_Expenses   \
        #reconciled_cost_of_revenue                                  =#Reconciled_Cost_of_Revenue   \
        #reconciled_depreciation                                     =#Reconciled_Depreciation   \
        #tax_effect_of_unusual_items                                 =#Tax_Effect_of_Unusual_Items   \
        profit_margin                                               =validate_api(['get-statistics','defaultKeyStatistics','profitMargin']),  \
        operating_margin_ttm                                        =validate_api(['get-statistics','financialData','operatingMargins']),   \
        #revenue_ttm                                                 =#Revenue_ttm  \
        revenue_per_share_ttm                                       =validate_api(['get-statistics','financialData','revenuePerShare']),   \
        quarterly_revenue_growth_yoy                                =validate_api(['get-statistics','financialData','revenueGrowth']),  \
        #gross_profit_ttm                                            =#Gross_Profit_ttm  \
        ebitda                                                      =validate_api(['get-statistics','financialData','ebitda']),  \
        net_income_avi_to_common_ttm                                =validate_api(['get-statistics','defaultKeyStatistics','netIncomeToCommon']),  \
        #diluted_eps_ttm                                             =#Diluted_EPS_ttm  \
        quarterly_earnings_growth_yoy                               =validate_api(['get-statistics','defaultKeyStatistics','earningsQuarterlyGrowth']),   \
        return_on_assets_ttm                                        =validate_api(['get-statistics','financialData','returnOnAssets']),  \
        return_on_equity_ttm                                        =validate_api(['get-statistics','financialData','returnOnEquity']),  \
        operating_cash_flow_ttm                                     =validate_api(['get-statistics','financialData','operatingCashflow']),  \
        levered_free_cash_flow_ttm                                  =validate_api(['get-statistics','financialData','freeCashflow']),   \
        fiscal_year_ends                                            =toDate(validate_api(['get-statistics','defaultKeyStatistics','nextFiscalYearEnd'])),    \
        
        most_recent_quarter_mrq                                     =toDate(validate_api(['get-statistics','defaultKeyStatistics','mostRecentQuarter'])),    \
        total_cash_mrq                                              =validate_api(['get-statistics','financialData','totalCash']),  \
        total_cash_per_share_mrq                                    =validate_api(['get-statistics','financialData','totalCashPerShare']),  \
        total_debt_mrq                                              =validate_api(['get-statistics','financialData','totalDebt']),  \
        total_debt_divided_equity_mrq                               =validate_api(['get-statistics','financialData','debtToEquity']),  \
        current_ratio_mrq                                           =validate_api(['get-statistics','financialData','currentRatio']),  \
        book_value_per_share_mrq                                    =validate_api(['get-statistics','defaultKeyStatistics','bookValue']),  \
        beta_5y_monthly                                             =validate_api(['get-statistics','summaryDetail','beta']),  \
        fifty_two_week_change                                       =validate_api(['get-statistics','defaultKeyStatistics','52WeekChange']),  \
        averagevolume                                               =validate_api(['get-statistics','summaryDetail','averageVolume']),  \
        fifty_two_week_high                                         =validate_api(['get-statistics','summaryDetail','FiftyTwoWeekHigh']),  \
        fifty_two_week_low                                          =validate_api(['get-statistics','summaryDetail','FiftyTwoWeekLow']),  \
        fifty_day_moving_average                                    =validate_api(['get-statistics','summaryDetail','FiftyDayAverage']),  \
        two_hundred_day_moving_average                              =validate_api(['get-statistics','summaryDetail','TwoHundredDayAverage']),  \
        #avg_vol_3_month                                             =#Avg_Vol_3_month  \
        avg_vol_ten_day                                             =validate_api(['get-statistics','summaryDetail','averageVolume10Day']),  \
        #shares_outstanding                                          =#Shares_Outstanding   \
        #stock_float                                                 =#Float  \
        #percentage_held_by_insiders                                 =#Percentage_Held_by_Insiders  \
        #percentage_held_by_institutions                             =#Percentage_Held_by_Institutions  \
        #shares_short                                                =#Shares_Short  \
        #short_ratio                                                 =#Short_Ratio  \
        #short_percentage_of_float                                   =#Short_Percentage_of_Float  \
        #short_percentage_of_shares_outstanding                      =#Short_Percentage_of_Shares_Outstanding  \
        #shares_short_prior                                          =#Shares_Short_Prior  \
        forward_annual_dividend_rate                                =validate_api(['get-statistics','summaryDetail','dividendRate']),  \
        forward_annual_dividend_yield                               =validate_api(['get-statistics','summaryDetail','dividendYield']),  \
        trailing_annual_dividend_rate                               =validate_api(['get-statistics','summaryDetail','payoutRatio']),  \
        trailing_annual_dividend_yield                              =validate_api(['get-statistics','calendarEvents','dividendDate']),  \
        five_year_average_dividend_yield                            =validate_api(['get-statistics','summaryDetail','trailingAnnualDividendRate']),  \
        payout_ratio                                                =validate_api(['get-statistics','summaryDetail','trailingAnnualDividendYield']),  \
        dividend_date                                               =toDate(validate_api(['get-statistics','summaryDetail','fiveYearAvgDividendYield']))    \
        #last_split_factor                                           =#Last_Split_Factor  \
        #last_split_date                                             =#Last_Split_Date  \
        )

        self.session.add (new_stock)
        self.session.commit()
        print("Everything was added to the database")
        
    #    conn = self.services.connecting_to_server()
    #    if self.already_exists_in_DB == False:
    #        with conn: 
    #            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    #                cur.execute("SELECT stock.ticker_symbol FROM stock")
    #                self.ticker_table = cur.fetchall()
    ##Data clups
    #                cur.execute('''
    #            INSERT INTO stock (
    #                ticker_symbol,
    #                stock_name,
    #                stock_price,
    #                previous_close,
    #                open,
    #                bid,
    #                bid_size,
    #                ask,
    #                ask_size,
    #                Days_Range_High,
    #                Days_Range_Low,
    #                Fifty_Two_Week_Range_High,
    #                Fifty_Two_Week_Range_Low,
    #                pe_ratio_ttm,
    #                EPS_TTM,
    #                Earnings_Date,
    #                Volume,
    #                Avg_Volume_3_Month,
    #                Market_Cap,
    #                Beta,
    #                One_year_Target_Est,
    #                Ex_Dividend_Date,
    #                Total_Revenue,
    #                Gross_Profit,
    #                Profit_Margin,
    #                Operating_Margin_ttm,
    #                Revenue_Per_Share_ttm,
    #                Quarterly_Revenue_Growth_yoy,
    #                EBITDA,
    #                Net_Income_Avi_to_Common_ttm,
    #                Quarterly_Earnings_Growth_yoy,
    #                Return_on_Assets_ttm,
    #                Return_on_Equity_ttm,
    #                Operating_Cash_Flow_ttm,
    #                Levered_Free_Cash_Flow_ttm,
    #                Fiscal_Year_Ends,
    #                Most_Recent_Quarter_mrq,
    #                Total_Cash_mrq,
    #                Total_Cash_Per_Share_mrq,
    #                Total_Debt_mrq,
    #                Total_Debt_DIVIDED_Equity_mrq,
    #                Current_Ratio_mrq,
    #                Book_Value_Per_Share_mrq,
    #                Beta_5Y_Monthly,
    #                Fifty_Two_Week_Change,
    #                averageVolume,
    #                Fifty_Two_Week_High,
    #                Fifty_Two_Week_Low,
    #                Fifty_Day_Moving_Average,
    #                Two_Hundred_Day_Moving_Average,
    #                Avg_Vol_Ten_day,
    #                Forward_Annual_Dividend_Rate,
    #                Forward_Annual_Dividend_Yield,
    #                Payout_Ratio,
    #                Dividend_Date,
    #                Trailing_Annual_Dividend_Rate,
    #                Trailing_Annual_Dividend_Yield,
    #                Five_Year_Average_Dividend_Yield
    #            ) values  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,#%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #            returning stock
    #            ''', (
    #                validate_api(['get-statistics','symbol']),
    #                validate_api(['get-statistics','quoteType','longName']),
    #                validate_api(['get-statistics','price','regularMarketPrice']),
    #                validate_api(['get-statistics','summaryDetail','regularMarketPreviousClose']),
    #                validate_api(['get-statistics','price','regularMarketOpen']),
    #                validate_api(['get-statistics','summaryDetail','bid']),
    #                validate_api(['get-statistics','summaryDetail','bidSize']),
    #                validate_api(['get-statistics','summaryDetail','ask']),
    #                validate_api(['get-statistics','summaryDetail','askSize']),
    #                validate_api(['get-statistics','summaryDetail','dayHigh']),
    #                validate_api(['get-statistics','summaryDetail','dayLow']),
    #                validate_api(['get-statistics','summaryDetail','fiftyTwoWeekHigh']),
    #                validate_api(['get-statistics','summaryDetail','fiftyTwoWeekLow']),
    #                validate_api(['get-statistics','summaryDetail','trailingPE']),
    #                validate_api(['get-statistics','defaultKeyStatistics','trailingEps']),
    #                validate_api(['get-statistics','calendarEvents','earnings','earningsDate']),
    #                validate_api(['get-statistics','summaryDetail','volume']),
    #                validate_api(['get-statistics','get-statistics','price','averageDailyVolume3Month']),
    #                validate_api(['get-statistics','price','marketCap']),
    #                #TBeta_5Y_Monthly
    #                #volatility
    #                validate_api(['get-statistics','defaultKeyStatistics','beta']),
    #                validate_api(['get-statistics','financialData','targetMeanPrice']),
    #                #Forward_Dividend_AND_Yield
    #                validate_api(['get-statistics','summaryDetail','exDividendDate']),
    #                #Basic_Average_Shares
    #                #Diluted_Average_Shares
    #                validate_api(['get-statistics','financialData','totalRevenue']),
    #                #Other_Income_Expense
    #                #Basic_EPS
    #                #Diluted_EPS
    #                #EBIT
    #                #Total_Unusual_Items_Excluding_Goodwill
    #                #Total_Unusual_Items
    #                validate_api(['get-statistics','financialData','grossProfits']),
    #                #Operating_Income
    #                #Pretax_Income
    #                #Net_Income_Common_Stockholders
    #                #Diluted_NI_Available_to_Com_Stockholders
    #                #Total_Operating_Income_as_Reported
    #                #Net_Income_from_Continuing_AND_Discontinued_Operation
    #                #Normalized_Income
    #                #Net_Income_from_Continuing_Operation_Net_Minority_Interest
    #                #Normalized_EBITDA
    #                #Cost_of_Revenue
    #                #Operating_Expense 
    #                #Tax_Provision
    #                #Total_Expenses 
    #                #Reconciled_Cost_of_Revenue 
    #                #Reconciled_Depreciation 
    #                #Tax_Effect_of_Unusual_Items 
    #                validate_api(['get-statistics','defaultKeyStatistics','profitMargin']),
    #                validate_api(['get-statistics','financialData','operatingMargins']), 
    #                #Revenue_ttm
    #                validate_api(['get-statistics','financialData','revenuePerShare']), 
    #                validate_api(['get-statistics','financialData','revenueGrowth']),
    #                #Gross_Profit_ttm
    #                validate_api(['get-statistics','financialData','ebitda']),
    #                validate_api(['get-statistics','defaultKeyStatistics','netIncomeToCommon']),
    #                #Diluted_EPS_ttm
    #                validate_api(['get-statistics','defaultKeyStatistics','earningsQuarterlyGrowth']), 
    #                validate_api(['get-statistics','financialData','returnOnAssets']),
    #                validate_api(['get-statistics','financialData','returnOnEquity']),
    #                validate_api(['get-statistics','financialData','operatingCashflow']),
    #                validate_api(['get-statistics','financialData','freeCashflow']),  
    #                validate_api(['get-statistics','defaultKeyStatistics','nextFiscalYearEnd']),
    #                validate_api(['get-statistics','defaultKeyStatistics','mostRecentQuarter']),
    #                validate_api(['get-statistics','financialData','totalCash']),
    #                validate_api(['get-statistics','financialData','totalCashPerShare']),
    #                validate_api(['get-statistics','financialData','totalDebt']),
    #                validate_api(['get-statistics','financialData','debtToEquity']),
    #                validate_api(['get-statistics','financialData','currentRatio']),
    #                validate_api(['get-statistics','defaultKeyStatistics','bookValue']),
    #                validate_api(['get-statistics','summaryDetail','beta']),
    #                validate_api(['get-statistics','defaultKeyStatistics','52WeekChange']),
    #                validate_api(['get-statistics','summaryDetail','averageVolume']),
    #                validate_api(['get-statistics','summaryDetail','FiftyTwoWeekHigh']),
    #                validate_api(['get-statistics','summaryDetail','FiftyTwoWeekLow']),
    #                validate_api(['get-statistics','summaryDetail','FiftyDayAverage']),
    #                validate_api(['get-statistics','summaryDetail','TwoHundredDayAverage']),
    #                #Avg_Vol_3_month
    #                validate_api(['get-statistics','summaryDetail','averageVolume10Day']),
    #                #Shares_Outstanding 
    #                #Float
    #                #Percentage_Held_by_Insiders
    #                #Percentage_Held_by_Institutions
    #                #Shares_Short
    #                #Short_Ratio
    #                #Short_Percentage_of_Float
    #                #Short_Percentage_of_Shares_Outstanding
    #                #Shares_Short_Prior
    #                validate_api(['get-statistics','summaryDetail','dividendRate']),
    #                validate_api(['get-statistics','summaryDetail','dividendYield']),
    #                validate_api(['get-statistics','summaryDetail','payoutRatio']),
    #                validate_api(['get-statistics','calendarEvents','dividendDate']),
    #                validate_api(['get-statistics','summaryDetail','trailingAnnualDividendRate']),
    #                validate_api(['get-statistics','summaryDetail','trailingAnnualDividendYield']),
    #                validate_api(['get-statistics','summaryDetail','fiveYearAvgDividendYield'])
    #                #Last_Split_Factor
    #                #Last_Split_Date
#
    #                #WITHOUT THE HASTAGES IT CONTAINS 59 LINES UNTIL HERE
#
#
    #                #SKIP FINANCIALS
    #                #OTHER INCOME EXPENSE
    #                #BASIC EPS
    #                #Diluted eps
    #                #Ebit
    #                #Totalunusual items goodwill
    #                #Totalunusual items
    #                #Cost of revenue
    #                #Expense
    #                #tax
    #                #Expenses
    #                #Reconsiled
    #                #Reconsiled
    #                #tax
    #            )
    #        )

    #                print(cur.fetchall())
    #                print("Everything was added to the database")

    #        conn.commit()
    #        conn.close()

        
                    

#server = Json_to_server()
#server.open_json_file('stock.json')
#server.checking_if_ticker_exists_in_database()
#server.connecting_to_server()



#all = [
 #   ['summaryDetails', 'bit'],
  #  ['summaryDetails', 'bitAsk'],
   # ['summaryDetails', 'bitHigh'],
  #  ['summaryDetails', 'bitHigh']
#]

#def validate_api():
 #   print()

#def validate_all_data():
#    for row in all:
        # row = ['summaryDetails', 'bit'],
 #       validate_api(['get-statistics', row[0], row[1]])


#def send_to_server():

 #   validate_all_data()
    
  #  write_to_sql()

  #Notes show 
    #Show the progress that I have made and what I have done so far 
    #In the Refactoring like he used git lab or so to show what was deleted and what hasnt 
