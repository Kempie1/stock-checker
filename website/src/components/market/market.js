import React, {  useState, useEffect  } from 'react';
import { BrowserRouter as Router, Link} from "react-router-dom"
import axios from 'axios'
import './market.css'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import { set } from 'lodash';



var loading= true


export function gainOrLoss(open,close,use){
  loading = false
  if(close-open<0){
    return "loss"
  }
  if(close-open>0){
    return "gain"
  }
  if(close-open===0){
    return "same"
  }
}

//returns the proper icon
export function differenceArrow(open,close){
  switch(gainOrLoss(open,close)){
    case "loss":
      return "fa-arrow-down"
    case "gain":
      return "fa-arrow-up"
    case "same":
      return "fa-equals"
  }
}

export function getAvailable(){
  return (axios.get(`https://stockcheckerdb.herokuapp.com/getavailable/`)
  )
}

export function makeBlocks(value){
  return (
  <Link to={"/stock/"+value[0]} id={value[0]}>
    <li key={value[0]} className="stock_block">
      <p>{value[1]}</p>
      <p>( {value[0]} )</p>
      <p>Day's Volume: {value[2]}</p>
      <p className={gainOrLoss(value[3],value[4])}>
        Day's change: {(value[4]-value[3]).toFixed(2)} 
        <i className={"fas "+differenceArrow(value[3],value[4])}></i>
      </p>
    </li>
  </Link>)
}


export const Market = (props) => {
  const [tickers, setTickers] = useState([])


  useEffect(()=>{
    if (!props.test){
    getAvailable().then(res => {
      setTickers(res.data.Stocks);
    }).catch(error => {
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
  }else{
    setTickers(props.tickers)
  }
}, [])


return (
  <div className="stock_blocks">
    {
      ((Array.isArray(tickers)) ?
      tickers.map((value) => {
        return makeBlocks(value)
      }): "error")
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
