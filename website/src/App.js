import React from 'react';
import Navbar from './components/navbar/Navbar';
import Login from "./components/Login";
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar/>
        <Switch>
          <Route path="/signin">
            <Login/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
