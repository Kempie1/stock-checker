from decouple import config
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 
from sqlalchemy import create_engine    

Base = declarative_base()   

class Stock(Base):  
    __tablename__                                               = "stock" 
    ticker_symbol                                               = Column(String(10),primary_key=True,nullable=False)
    stock_name                                                  = Column(String(255),nullable=False)
    stock_price                                                 = Column(String(255))
    previous_close                                              = Column(String(255))
    open_bid                                                    = Column(String(255))     
    bid                                                         = Column(String(255))
    bid_size                                                    = Column(String(255))
    ask                                                         = Column(String(255))
    ask_size                                                    = Column(String(255))
    days_range_high                                             = Column(String(255))
    days_range_low                                              = Column(String(255))
    fifty_two_week_range_high                                   = Column(String(255))
    fifty_two_week_range_low                                    = Column(String(255))
    pe_ratio_ttm                                                = Column(String(255))
    eps_ttm                                                     = Column(String(255))
    earnings_date                                               = Column(String(255))
    volume                                                      = Column(String(255))
    avg_volume_3_month                                          = Column(String(255))
    market_cap                                                  = Column(String(255))
    beta                                                        = Column(String(255))
    one_year_target_est                                         = Column(String(255))
    ex_dividend_date                                            = Column(String(255))
    total_revenue                                               = Column(String(255))
    gross_profit                                                = Column(String(255))
    profit_margin                                               = Column(String(255))
    operating_margin_ttm                                        = Column(String(255))
    revenue_per_share_ttm                                       = Column(String(255))
    quarterly_revenue_growth_yoy                                = Column(String(255))
    ebitda                                                      = Column(String(255))
    net_income_avi_to_common_ttm                                = Column(String(255))
    quarterly_earnings_growth_yoy                               = Column(String(255))
    return_on_assets_ttm                                        = Column(String(255))
    return_on_equity_ttm                                        = Column(String(255))
    operating_cash_flow_ttm                                     = Column(String(255))
    levered_free_cash_flow_ttm                                  = Column(String(255))
    fiscal_year_ends                                            = Column(String(255))
    most_recent_quarter_mrq                                     = Column(String(255))
    total_cash_mrq                                              = Column(String(255))
    total_cash_per_share_mrq                                    = Column(String(255))
    total_debt_mrq                                              = Column(String(255))
    total_debt_divided_equity_mrq                               = Column(String(255))
    current_ratio_mrq                                           = Column(String(255))
    book_value_per_share_mrq                                    = Column(String(255))
    beta_5y_monthly                                             = Column(String(255))
    fifty_two_week_change                                       = Column(String(255))
    averagevolume                                               = Column(String(255))
    fifty_two_week_high                                         = Column(String(255))
    fifty_two_week_low                                          = Column(String(255))
    fifty_day_moving_average                                    = Column(String(255))
    two_hundred_day_moving_average                              = Column(String(255))
    avg_vol_ten_day                                             = Column(String(255))
    forward_annual_dividend_rate                                = Column(String(255))
    forward_annual_dividend_yield                               = Column(String(255))
    trailing_annual_dividend_rate                               = Column(String(255))
    trailing_annual_dividend_yield                              = Column(String(255))
    five_year_average_dividend_yield                            = Column(String(255))
    payout_ratio                                                = Column(String(255))
    dividend_date                                               = Column(String(255))

class Chart(Base):
    __tablename__                                               = "chart"
    id                                                          = Column(Integer, primary_key=True)
    time                                                        = Column(String(255))
    open_bid                                                    = Column(String(255))
    volume                                                      = Column(String(255))
    low                                                         = Column(String(255))
    high                                                        = Column(String(255))
    close                                                       = Column(String(255))
    ticker_symbol                                               = Column(String(10),ForeignKey('stock.ticker_symbol'),nullable=False)
    ticker                                                      = relationship('Stock', foreign_keys='Chart.ticker_symbol')


engine = create_engine(config("DB_URL"))

#Create all tables in the engine.
Base.metadata.create_all(engine)