from flask import Flask, json

app = Flask(__name__)


@app.route('/json', methods=['POST', 'GET'])
def mock_api():
    null = None
    data = {"ask":"685.77","ask_size":"3200","averagevolume":"34328526","avg_vol_ten_day":null,"avg_volume_3_month":null,"beta":"2.010479","beta_5y_monthly":"2.010479","bid":"686.83","bid_size":"1000","book_value_per_share_mrq":"23.901","current_ratio_mrq":"1.661","days_range_high":"706","days_range_low":"682.46","dividend_date":null,"earnings_date":"1626739200","ebitda":"4551000064","eps_ttm":"0.998","ex_dividend_date":null,"fifty_day_moving_average":null,"fifty_two_week_change":"3.6600718","fifty_two_week_high":null,"fifty_two_week_low":null,"fifty_two_week_range_high":"900.4","fifty_two_week_range_low":"139.6","fiscal_year_ends":"1672444800","five_year_average_dividend_yield":null,"forward_annual_dividend_rate":null,"forward_annual_dividend_yield":null,"gross_profit":"6630000000","levered_free_cash_flow_ttm":"3538249984","market_cap":"662164144128","most_recent_quarter_mrq":"1617148800","net_income_avi_to_common_ttm":"1112000000","one_year_target_est":"636.35","open_bid":"703.8","operating_cash_flow_ttm":"8024000000","operating_margin_ttm":"0.06013","payout_ratio":"0","pe_ratio_ttm":"688.7475","previous_close":"709.44","profit_margin":null,"quarterly_earnings_growth_yoy":"26.375","quarterly_revenue_growth_yoy":"0.736","return_on_assets_ttm":"0.02994","return_on_equity_ttm":"0.0716","revenue_per_share_ttm":"38.052","stock_name":"Tesla, Inc.","stock_price":"687.37","ticker_symbol":"TSLA","total_cash_mrq":"17141000192","total_cash_per_share_mrq":"17.793","total_debt_divided_equity_mrq":"51.138","total_debt_mrq":"12510999552","total_revenue":"35939999744","trailing_annual_dividend_rate":null,"trailing_annual_dividend_yield":null,"two_hundred_day_moving_average":null,"volume":"16201842"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# Run in HTTP
app.run(host='127.0.0.1', port='5000')  