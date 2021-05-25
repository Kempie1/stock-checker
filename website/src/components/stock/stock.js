import React, {  useState, useEffect  } from 'react';
import { BrowserRouter as Router, useParams } from "react-router-dom";
import axios from 'axios'
import './stock.css'
import {stockPlaceholder} from "./stockPlaceholder"
import Tabs from "./tabs/tabs"; 
import chartPlaceholder from './stockCharts.jpg'

export function getStock(param){
  return (axios.get(`https://stockcheckerdb.herokuapp.com/getst/?ticker=${param}`)
  )
}

export function timeConverter(UNIX_timestamp){
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var time = date + ' ' + month + ' ' + year;
  return time;
}

export function format(string) {
  string=string.split('_').join(' ')
  return string.charAt(0).toUpperCase() + string.slice(1);
}

const Stock = () => {
  const params = useParams().ticker
  const [ticker, setTicker] = useState(stockPlaceholder)

  useEffect(()=>{
    getStock(params)
    .then(res => {
      setTicker(res.data);
    })
    .catch(error => {
      if (error.response) {
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        console.log(error.request);
      } else {
        console.log('Error', error.message);
      }
    }
    );
    }, [])

  

  
return (
  
    <div className="stock_data">
      <div className="block-shadow">
        <h2>{ticker.stock_name}</h2>
        <p>{ticker.ticker_symbol}</p>
        <ul className="mainData">
          <p>Current Price: {ticker.stock_price}</p>
          <p>Previous close: {ticker.previous_close}</p>
          <Tabs> 
            <div label="Basic Information"> 
            {
          Object.entries(ticker).map(([key, value]) => {
            if (key==='dividend_date'|| key==='earnings_date' || key==='ex_dividend_date' || key==='fiscal_year_ends' || key=== 'most_recent_quarter_mrq' || key==='stock_name'|| key==='ticker_symbol' ||  key==='gross_profit'|| key==='levered_free_cash_flow_ttm' || key==='market_cap' ||    key==='net_income_avi_to_common_ttm' || key=== 'one_year_target_est' || key=== 'operating_cash_flow_ttm'  || key=== 'operating_margin_ttm'  || key=== 'payout_ratio'  || key=== 'quarterly_earnings_growth_yoy'  || key=== 'quarterly_revenue_growth_yoy'  || key=== 'return_on_assets_ttm'  || key=== 'return_on_equity_ttm'  || key=== 'revenue_per_share_ttm'  || key=== 'total_cash_mrq'  || key=== 'total_cash_per_share_mrq'  || key=== 'total_debt_divided_equity_mrq'  || key=== 'total_debt_mrq'  || key=== 'total_revenue'  || key=== 'trailing_annual_dividend_rate'  || key=== 'trailing_annual_dividend_yield'  ){
              return null
            }
            if (value==null){
              return <li>{format(key)}: Data is unavailable</li>}
            return <li>{format(key)}: {value}</li>
        })} 
            </div> 

            
            <div label="Croc"> 
            {
              Object.entries(ticker).map(([key, value]) => {

                if (key==='gross_profit'|| key==='levered_free_cash_flow_ttm' || key==='market_cap' ||    key==='net_income_avi_to_common_ttm' || key=== 'one_year_target_est' || key=== 'operating_cash_flow_ttm'  || key=== 'operating_margin_ttm'  || key=== 'payout_ratio'  || key=== 'quarterly_earnings_growth_yoy'  || key=== 'quarterly_revenue_growth_yoy'  || key=== 'return_on_assets_ttm'  || key=== 'return_on_equity_ttm'  || key=== 'revenue_per_share_ttm'  || key=== 'total_cash_mrq'  || key=== 'total_cash_per_share_mrq'  || key=== 'total_debt_divided_equity_mrq'  || key=== 'total_debt_mrq'  || key=== 'total_revenue'  || key=== 'trailing_annual_dividend_rate'  || key=== 'trailing_annual_dividend_yield'  ){
                  return <li>{format(key)}: {value}</li>
                }
            })} 
            </div> 


            <div label="Important Dates"> 
            {
              Object.entries(ticker).map(([key, value]) => {
               
                if (key==='dividend_date'|| key==='earnings_date' || key==='ex_dividend_date' ||    key==='fiscal_year_ends' || key=== 'most_recent_quarter_mrq' ){
                  if (value==null){
                    return <li>{format(key)}: Data is unavailable</li>}
                  return <li>{format(key)}: {timeConverter(value)}</li>
                }
                
            })} 
            </div> 
          </Tabs> 
          
        </ul>
      </div>
      <img src={chartPlaceholder} className="chart"/>
    </div>
    
  );
};

export default Stock;