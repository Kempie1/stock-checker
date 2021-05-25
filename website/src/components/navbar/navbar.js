import React, { Component } from 'react';
import {MenuItems} from "./menuItems"
import {Button} from '../button/button'
import './navbar.css'
import {  Link  } from "react-router-dom";


import Search from './searchbar/search'



class Navbar extends Component {
    state = { clicked:false }

    

    handleClick = () =>{
        this.setState({ clicked: !this.state.clicked })
    }

  
    whatButton = () =>{
        if(this.props.user===null)
        {
            return (
        <Link to="/login">
            <Button>Sign In</Button>
        </Link>)
        }
        else{
            return (
                <Link to="/profile">
                    <Button>Profile</Button>
                </Link>
            )
        }
    }



    render(){
        return(
            <nav className="NavbarItems">
                <Link to="/stock-checker"><h1 className="navbar-logo">StockChecker</h1></Link>
                <div className="menu-icon" onClick={this.handleClick}>
                    <i className={this.state.clicked ? 'fas fa-timeys' : 'fas fa-bars'}></i>
                </div>
                <ul className={this.state.clicked ? 'nav-menu active': 'nav-menu'}>
                    {MenuItems.map((item,index)=>{
                        return (
                            <li key={index} id={item.idN}>
                                <Link className={item.cName} to={item.url} id={item.idN}>
                                    {item.title}
                                </Link>
                            </li>
                        )
                    })}

            </ul>
                <Search/>
                {this.whatButton()}
                
            </nav>
        )
    }
}

export default Navbar