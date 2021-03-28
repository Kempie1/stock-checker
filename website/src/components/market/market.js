import React, {  useState  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, useHistory } from "react-router-dom"


const Market = (props) => {
const [error, setError] = useState("")
const { currentUser} = useAuth()




return (
    <div>
    
    <h1>APPLE</h1>
    </div>
    
  );
};

export default Market;