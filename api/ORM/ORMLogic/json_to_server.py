#External
import psycopg2
import psycopg2.extras
import json
import requests
from json.decoder import JSONDecodeError
import os
from decouple import config
#Internal
from api_call_to_json import Api_call
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarative import Stock, Base
from datetime import datetime

class Json_to_server():
    
    def __init__(self):
        engine = create_engine(config("DB_URL"))
        Base.metadata.bind = engine
        self.DBSession = sessionmaker(bind=engine)
    
    def open_json_file(self, json_file):
        if os.path.getsize(json_file)>40:
            json_data = open(json_file,"r")
            self.data = json.load(json_data)
            return True
        print("Stock.json is empty \nStock wasn't added to the database")
        return False

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

        self.session=self.DBSession()

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
        earnings_date                                               =validate_api(['get-statistics','calendarEvents','earnings','earningsDate']),   \
        volume                                                      =validate_api(['get-statistics','summaryDetail','volume']),  \
        avg_volume_3_month                                          =validate_api(['get-statistics','get-statistics','price','averageDailyVolume3Month']),  \
        market_cap                                                  =validate_api(['get-statistics','price','marketCap']),  \
        beta                                                        =validate_api(['get-statistics','defaultKeyStatistics','beta']),  \
        one_year_target_est                                         =validate_api(['get-statistics','financialData','targetMeanPrice']),  \
        ex_dividend_date                                            =validate_api(['get-statistics','summaryDetail','exDividendDate']),  \
        total_revenue                                               =validate_api(['get-statistics','financialData','totalRevenue']),  \
        gross_profit                                                =validate_api(['get-statistics','financialData','grossProfits']),  \
        profit_margin                                               =validate_api(['get-statistics','defaultKeyStatistics','profitMargin']),  \
        operating_margin_ttm                                        =validate_api(['get-statistics','financialData','operatingMargins']),   \
        revenue_per_share_ttm                                       =validate_api(['get-statistics','financialData','revenuePerShare']),   \
        quarterly_revenue_growth_yoy                                =validate_api(['get-statistics','financialData','revenueGrowth']),  \
        ebitda                                                      =validate_api(['get-statistics','financialData','ebitda']),  \
        net_income_avi_to_common_ttm                                =validate_api(['get-statistics','defaultKeyStatistics','netIncomeToCommon']),  \
        quarterly_earnings_growth_yoy                               =validate_api(['get-statistics','defaultKeyStatistics','earningsQuarterlyGrowth']),   \
        return_on_assets_ttm                                        =validate_api(['get-statistics','financialData','returnOnAssets']),  \
        return_on_equity_ttm                                        =validate_api(['get-statistics','financialData','returnOnEquity']),  \
        operating_cash_flow_ttm                                     =validate_api(['get-statistics','financialData','operatingCashflow']),  \
        levered_free_cash_flow_ttm                                  =validate_api(['get-statistics','financialData','freeCashflow']),   \
        fiscal_year_ends                                            =validate_api(['get-statistics','defaultKeyStatistics','nextFiscalYearEnd']),    \
        most_recent_quarter_mrq                                     =validate_api(['get-statistics','defaultKeyStatistics','mostRecentQuarter']),    \
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
        avg_vol_ten_day                                             =validate_api(['get-statistics','summaryDetail','averageVolume10Day']),  \
        forward_annual_dividend_rate                                =validate_api(['get-statistics','summaryDetail','dividendRate']),  \
        forward_annual_dividend_yield                               =validate_api(['get-statistics','summaryDetail','dividendYield']),  \
        trailing_annual_dividend_rate                               =validate_api(['get-statistics','summaryDetail','trailingAnnualDividendRate']),  \
        trailing_annual_dividend_yield                              =validate_api(['get-statistics','summaryDetail','trailingAnnualDividendYield']),  \
        five_year_average_dividend_yield                            =validate_api(['get-statistics','summaryDetail','fiveYearAvgDividendYield']),   \
        payout_ratio                                                =validate_api(['get-statistics','summaryDetail','payoutRatio']),  \
        dividend_date                                               =validate_api(['get-statistics','calendarEvents','dividendDate'])  \
        )

        self.session.add (new_stock)
        #cursor = self.data
        #cursor = cursor.get(chart)
        #cursor = cursor.get(result)
        #if isinstance(cursor, list):
        #    cursor=cursor[0]
        #
        #while(not done)
        ##new_chart=( \
        ##time                                                        = 
        #open_bid                                                    = 
        #volume                                                      = 
        #low                                                         = 
        #high                                                        = 
        #close                                                       = 
        #ticker_symbol                                               = 
        #)


        self.session.commit()
        print(f"{validate_api(['get-statistics','quoteType','longName'])} Data has been added to the database")
        
    
