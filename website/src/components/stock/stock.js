import React, {  useState, useEffect  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Route, Link, Switch, useParams } from "react-router-dom";
import axios from 'axios'
import './stock.css'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";

const Stock = () => {
  const params = useParams().ticker
  const [ticker, setTicker] = useState({})
  const { currentUser } = useAuth()
  let loading=true

  useEffect(()=>{
    axios.get(`https://stockcheckerdb.herokuapp.com/getst/?ticker=${params}`)
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

  function timeConverter(UNIX_timestamp){
    loading=false
    var a = new Date(UNIX_timestamp * 1000);
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();

    var time = date + ' ' + month + ' ' + year;
    return time;
  }

  
return (
  
    <div>
      
      <div className="block-shadow">
      <Loader
        className="loader"
        visible={loading}
        type="Circles"
        color="#063D74"
        height={100}
        width={100}
      />
        <h2>{ticker.stock_name}</h2>
        <p>{ticker.ticker_symbol}</p>
        <ul className="mainData">
          <p>{ticker.stock_price}</p>
          <p>{ticker.previous_close}</p>
          <p>{ticker.bid}</p>
          {
          Object.entries(ticker).map(([key, value]) => {
            loading=false;
            if (value==null){
              return null}
            if (key==='dividend_date'|| key==='earnings_date' || key==='ex_dividend_date' || key==='fiscal_year_ends' || key=== 'most_recent_quarter_mrq' ){
              console.log(key)
              console.log(value)
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