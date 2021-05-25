import React from  "react";
import Navbar from "./components/navbar/navbar";
import Login from  "./components/login/login";
import Market from "./components/market/market";
import Stock from  "./components/stock/stock";
import Learning from "./components/learning/learning";
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
              <Market test={false}/>
            </Route>
            <Route path="/learning">
              <Learning/>
            </Route>
            <Route path="/stock/:ticker">
              <Stock/>
            </Route>
            <Route path="/login">
            {(currentUser!=null) ? <Redirect to="/profile" /> : <Login/>}
            </Route>
            <Route path="/profile">
              {(currentUser==null) ? <Redirect to="/login" /> : <Profile/>}
            </Route>
          </Switch>
        </div>
      </Router>
  );
}

export default App;
