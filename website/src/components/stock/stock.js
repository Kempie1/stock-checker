import React, {  useState  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Route, Link, Switch, useParams } from "react-router-dom";

const Stock = () => {
const [error, setError] = useState("")
const { currentUser} = useAuth()
const current=useParams()
console.log(current)


return (
    <div>
    <h1>You are not supposed to be here</h1>
    <h2>{current.ticker}</h2>

    </div>
    
  );
};

export default Stock;