import React, {  useState, useEffect  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Route, Link, Switch, useParams } from "react-router-dom";
import axios from 'axios'
import './stock.css'

const Stock = () => {
  const params = useParams().ticker
  const [ticker, setTicker] = useState({})
  const { currentUser } = useAuth()

  useEffect(()=>{
    axios.get(`https://stockcheckerdb.herokuapp.com/getst/?ticker=${params}`)
    .then(res => {
      console.log(res);
      setTicker(res.data);
      console.log(ticker);
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
    <div>
      <div className="block-shadow">
        <h2>{ticker.stock_name}</h2>
        
      </div>
    </div>
    
  );
};

export default Stock;