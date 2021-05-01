from decouple import config
import sys
from sqlalchemy import Column, Integer, Date, Numeric, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 
from sqlalchemy import create_engine    

Base = declarative_base()   

class Stock(Base):  
    __tablename__                                               = "stock" 
    ticker_symbol                                               = Column(String(10),primary_key=True,nullable=False)
    stock_name                                                  = Column(String(255),nullable=False)
    stock_price                                                 = Column(Numeric)
    previous_close                                              = Column(Numeric)
    open_bid                                                    = Column(Numeric)     
    bid                                                         = Column(Numeric)
    bid_size                                                    = Column(Numeric)
    ask                                                         = Column(Numeric)
    ask_size                                                    = Column(Numeric)
    days_range_high                                             = Column(Numeric)
    days_range_low                                              = Column(Numeric)
    fifty_two_week_range_high                                   = Column(Numeric)
    fifty_two_week_range_low                                    = Column(Numeric)
    pe_ratio_ttm                                                = Column(Numeric)
    eps_ttm                                                     = Column(Numeric)
    earnings_date                                               = Column(Date)
    volume                                                      = Column(Numeric)
    avg_volume_3_month                                          = Column(Numeric)
    market_cap                                                  = Column(Numeric)
    beta                                                        = Column(Numeric)
    one_year_target_est                                         = Column(Numeric)
    ex_dividend_date                                            = Column(Date)
    total_revenue                                               = Column(Numeric)
    gross_profit                                                = Column(Numeric)
    profit_margin                                               = Column(Numeric)
    operating_margin_ttm                                        = Column(Numeric)
    revenue_per_share_ttm                                       = Column(Numeric)
    quarterly_revenue_growth_yoy                                = Column(Numeric)
    ebitda                                                      = Column(Numeric)
    net_income_avi_to_common_ttm                                = Column(Numeric)
    quarterly_earnings_growth_yoy                               = Column(Numeric)
    return_on_assets_ttm                                        = Column(Numeric)
    return_on_equity_ttm                                        = Column(Numeric)
    operating_cash_flow_ttm                                     = Column(Numeric)
    levered_free_cash_flow_ttm                                  = Column(Numeric)
    fiscal_year_ends                                            = Column(Date)
    most_recent_quarter_mrq                                     = Column(Date)
    total_cash_mrq                                              = Column(Numeric)
    total_cash_per_share_mrq                                    = Column(Numeric)
    total_debt_mrq                                              = Column(Numeric)
    total_debt_divided_equity_mrq                               = Column(Numeric)
    current_ratio_mrq                                           = Column(Numeric)
    book_value_per_share_mrq                                    = Column(Numeric)
    beta_5y_monthly                                             = Column(Numeric)
    fifty_two_week_change                                       = Column(Numeric)
    averagevolume                                               = Column(Numeric)
    fifty_two_week_high                                         = Column(Numeric)
    fifty_two_week_low                                          = Column(Numeric)
    fifty_day_moving_average                                    = Column(Numeric)
    two_hundred_day_moving_average                              = Column(Numeric)
    avg_vol_ten_day                                             = Column(Numeric)
    forward_annual_dividend_rate                                = Column(Numeric)
    forward_annual_dividend_yield                               = Column(Numeric)
    trailing_annual_dividend_rate                               = Column(Numeric)
    trailing_annual_dividend_yield                              = Column(Numeric)
    five_year_average_dividend_yield                            = Column(Numeric)
    payout_ratio                                                = Column(Numeric)
    dividend_date                                               = Column(Date)

class Chart(Base):
    __tablename__                                               = "chart"
    id                                                          = Column(Integer, primary_key=True)
    time                                                        = Column(Date)
    open_bid                                                    = Column(Numeric)
    volume                                                      = Column(Numeric)
    low                                                         = Column(Numeric)
    high                                                        = Column(Numeric)
    close                                                       = Column(Numeric)
    ticker_symbol                                               = Column(String(10),ForeignKey('stock.ticker_symbol'),nullable=False)
    ticker                                                      = relationship('Stock', foreign_keys='Chart.ticker_symbol')


engine = create_engine(config("DB_URL"))

#Create all tables in the engine.
Base.metadata.create_all(engine)