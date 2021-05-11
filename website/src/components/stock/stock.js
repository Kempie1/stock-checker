import React, {  useState, useEffect  } from 'react';
import { BrowserRouter as Router, useParams } from "react-router-dom";
import axios from 'axios'
import './stock.css'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";

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

const Stock = () => {
  const params = useParams().ticker
  const [ticker, setTicker] = useState({})

  useEffect(()=>{
    getStock(params)
    .then(res => {
      setTicker(res.data);
    })
    .catch(error => {
      if (error.response) {
        // Request made and server responded
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        console.log(error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
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
          <p>{ticker.stock_price}</p>
          <p>{ticker.previous_close}</p>
          <p>{ticker.bid}</p>
          {
          Object.entries(ticker).map(([key, value]) => {
            if (value==null){
              return null}
            if (key==='dividend_date'|| key==='earnings_date' || key==='ex_dividend_date' || key==='fiscal_year_ends' || key=== 'most_recent_quarter_mrq' ){
              return <li>{key}: {timeConverter(value)}</li>
            }
            return <li>{key}: {value}</li>
        })}
        </ul>
      </div>
    </div>
    
  );
};

export default Stock;