import React, {  useState, useEffect  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Link, useHistory } from "react-router-dom"
import axios from 'axios'

const Market = (props) => {
const [tickers, setTickers] = useState("")
const { currentUser} = useAuth()

useEffect(()=>{
  axios.get(`https://stockcheckerdb.herokuapp.com/getavailable/`)
  .then(res => {
    setTickers(res.data.Stocks);
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
//[Array(1), Array(1), Array(1)]
function listStocks(){
  //limit 10
  //var count = 0
  if (Array.isArray(tickers)){
  tickers.map((value) => {
    console.log(value[0])
    return <p>{value}</p>}
  )
  }
  }



return (
    <div>
    <Link to="/stock/AAPL">
      Apple
    </Link>
    {listStocks()}
    </div>
    
  );
};

export default Market;