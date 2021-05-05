import React from  "react";
import Navbar from "./components/navbar/navbar";
import Login from  "./components/login/login";
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
          <Navbar user={currentUser}/>
          <Switch>
            <Route path="/stock-checker" exact ={true}>
              <Market/>
            </Route>
            <Route path="/stock-checker/stock/:ticker">
              <Stock/>
            </Route>
            <Route path="/stock-checker/login">
            {(currentUser!=null) ? <Redirect to="/stock-checker/profile" /> : <Login/>}
            </Route>
            <Route path="/stock-checker/profile">
              {(currentUser==null) ? <Redirect to="/stock-checker/login" /> : <Profile/>}
            </Route>
          </Switch>
        </div>
      </Router>
  );
}

export default App;
