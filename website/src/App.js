import React from  "react";
import Navbar from "./components/navbar/Navbar";
import Login from  "./components/Login/Login";
import Market from "./components/market/market";
import Stock from  "./components/stock/stock";
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";
import {  useAuth  } from "./providers/AuthProvider"
import Profile from "./components/profile/profile"



function App() {
  const { currentUser } = useAuth()

  return (
      <Router>
        <div className="App">
          <Navbar/>
          <Switch>
            <Route path="/" exact ={true}>
              <Market/>
            </Route>
            <Route path="/stock/:ticker">
              <Stock/>
            </Route>
            <Route path="/login">
              <Login/>
            </Route>
            <Route path="/profile">
              {(currentUser==null) ? <Redirect to="/" /> : <Profile/>}
            </Route>
          </Switch>
        </div>
      </Router>
  );
}

export default App;
