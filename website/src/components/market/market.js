import React, {  useState  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, Link, useHistory } from "react-router-dom"


const Market = (props) => {
const [error, setError] = useState("")
const { currentUser} = useAuth()




return (
    <div>
    <Link to="/stock/AAPL">
      Apple
    </Link>
    
    </div>
    
  );
};

export default Market;