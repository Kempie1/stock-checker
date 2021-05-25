import React, {  useState, useEffect  } from 'react';
import { useHistory } from "react-router-dom";
import axios from 'axios'
import Select from "react-dropdown-select";
import './search.css'
import {withRouter} from 'react-router';

export function getAvailable(){
  return (axios.get(`https://stockcheckerdb.herokuapp.com/getavailable/`)
  )
}

function Search() {
  let history = useHistory();
  const [stockList, setStockList] = useState([])

  useEffect(()=>{
    getAvailable().then(res => {
      var stocks=res.data.Stocks
      var tickerList=[]
      stocks.forEach(stock => tickerList.push({ label: `${stock[1]} (${stock[0]})`, value: stock[0]}))
      
      setStockList(tickerList);
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
  }, [])

  const change=(option)=>{
    console.log(option[0])
    history.replace(`/stock/${option[0].value}`)
    window.location.reload(false);
  }


  return (
    <div className="search">
      <Select
        options={stockList}
        dropdownHandle={false}
        onChange={opt => change(opt)}
      />
    </div>
  );
}

export default withRouter(Search);