import React, {  useState, useEffect  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Link} from "react-router-dom"
import axios from 'axios'
import './market.css'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";

const Market = (props) => {
const [tickers, setTickers] = useState([])
const { currentUser} = useAuth()
var loading= true

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

function gainOrLoss(open,close){
  loading = false
  if(close-open>0){
    return "loss"
  }
  if(close-open<0){
    return "gain"
  }
  if(close-open===0){
    return "same"
  }
}


//returns the proper icon
function differenceArrow(open,close){
  if(close-open>0){
    return "fa-arrow-down"
  }
  if(close-open<0){
    return "fa-arrow-up"
  }
  if(close-open===0){
    return "fa-equals"
  }
}
//repeated multiple times for extra icons
return (
    <div className="stock_blocks">
    {
      tickers.map((value) => {
        return (
        <Link to={"/stock/"+value[0]}>
          <li key={value[0]} className="stock_block">
            <p>{value[1]}</p>
            <p>({value[0]})</p>
            <p>Day's Volume: {value[2]}</p>
            <p className={gainOrLoss(value[4],value[3])}>Day's change: {(value[4]-value[3]).toFixed(2)} <i className={"fas "+differenceArrow(value[4],value[3])}></i></p>
            </li>
        </Link>
        )
      })
    }
    {
      tickers.map((value) => {
        return (
        <Link to={"/stock/"+value[0]}>
          <li key={value[0]+10} className="stock_block">
            <p>{value[1]}</p>
            <p>({value[0]})</p>
            <p>Day's Volume: {value[2]}</p>
            <p className={gainOrLoss(value[4],value[3])}>Day's change: {(value[4]-value[3]).toFixed(2)} <i className={"fas "+differenceArrow(value[4],value[3])}></i></p>
            </li>
        </Link>
        )
      })
    }
    {
      tickers.map((value) => {
        return (
        <Link to={"/stock/"+value[0]}>
          <li key={value[0]+20} className="stock_block">
            <p>{value[1]}</p>
            <p>({value[0]})</p>
            <p>Day's Volume: {value[2]}</p>
            <p className={gainOrLoss(value[4],value[3])}>Day's change: {(value[4]-value[3]).toFixed(2)} <i className={"fas "+differenceArrow(value[4],value[3])}></i></p>
            </li>
        </Link>
        )
      })
    }
    <Loader
        className="loader"
        visible={loading}
        type="Circles"
        color="#063D74"
        height={100}
        width={100}
      />
    </div>
    
  );
};

export default Market;