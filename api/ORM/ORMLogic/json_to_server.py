import psycopg2
import psycopg2.extras
import json
import requests
from json.decoder import JSONDecodeError
import os
from decouple import config
#from ORM_services import ORM_services
from api_call_to_json import Api_call
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarative import Stock, Base
from datetime import datetime

class Json_to_server():
    
    def __init__(self):
        engine = create_engine(config("DB_URL"))
    #    self.services = ORM_services()
        Base.metadata.bind = engine
        self.DBSession = sessionmaker(bind=engine)
        

    
    def open_json_file(self, json_file):
        if os.path.getsize(json_file)>40:
            json_data = open(json_file,"r")
            self.data = json.load(json_data)
            return True
        print("Stock.json is empty \nStock wasn't added to the database")
        return False

        

    #def checking_if_ticker_exists_in_database(self, ticker_symbol):
    #    self.already_exists_in_DB = self.services.checking_if_ticker_exists(ticker_symbol, ['REALCASE'])

    def send_data_to_server(self):
        
        def validate_api(l):
            cursor=self.data
            for x in range(len(l)):
                if x==(len(l)-1):
                    if l[x] in cursor:
                        cursor=cursor.get(l[x])
                        if not cursor:
                            return None
                        if 'raw' in cursor:
                            return cursor.get('raw')
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
        #new_chart
        self.session.commit()
        print(f"{validate_api(['get-statistics','quoteType','longName'])} Data has been added to the database")
        
    