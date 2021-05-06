from flask import Flask, json

app = Flask(__name__)

@app.route('/json', methods=['POST', 'GET'])
def test_json():
    null = None
    data = {"ask":"132.85","ask_size":"2900","averagevolume":"101384586","avg_vol_ten_day":null,"avg_volume_3_month":null,"beta":"1.219525","beta_5y_monthly":"1.219525","bid":"132.84","bid_size":"1400","book_value_per_share_mrq":"4.146","current_ratio_mrq":"1.142","days_range_high":"134.07","days_range_low":"131.83","dividend_date":"1620864000","earnings_date":"1627430400","ebitda":"99820003328","eps_ttm":"4.449","ex_dividend_date":"1620345600","fifty_day_moving_average":null,"fifty_two_week_change":"0.7936963","fifty_two_week_high":null,"fifty_two_week_low":null,"fifty_two_week_range_high":"145.09","fifty_two_week_range_low":"71.58","fiscal_year_ends":"1664150400","five_year_average_dividend_yield":"1.37","forward_annual_dividend_rate":"0.88","forward_annual_dividend_yield":"0.0067000003","gross_profit":"104956000000","levered_free_cash_flow_ttm":"80121004032","market_cap":"2228872019968","most_recent_quarter_mrq":"1616803200","net_income_avi_to_common_ttm":"76311003136","one_year_target_est":"157.7","open_bid":"132.04","operating_cash_flow_ttm":"99590995968","operating_margin_ttm":"0.27321","payout_ratio":"0.1834","pe_ratio_ttm":"29.841537","previous_close":"131.46","profit_margin":null,"quarterly_earnings_growth_yoy":"1.101","quarterly_revenue_growth_yoy":"0.536","return_on_assets_ttm":"0.169","return_on_equity_ttm":"1.034","revenue_per_share_ttm":"19.143","stock_name":"Apple Inc.","stock_price":"132.765","ticker_symbol":"AAPL","total_cash_mrq":"69833998336","total_cash_per_share_mrq":"4.185","total_debt_divided_equity_mrq":"175.843","total_debt_mrq":"121644998656","total_revenue":"325405999104","trailing_annual_dividend_rate":"0.82","trailing_annual_dividend_yield":"0.0062376386","two_hundred_day_moving_average":null,"volume":"41600271"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
    
# Run in HTTP
app.run(host='127.0.0.1', port='5000')  