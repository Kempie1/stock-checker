import React, { Component } from 'react';
import {MenuItems} from "./menuItems"
import {Button} from '../Button/Button'
import './navbar.css'
import {  Link  } from "react-router-dom";


class Navbar extends Component {
    state = { clicked:false, }

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
                <Link to="/"><h1 className="navbar-logo">StockChecker</h1></Link>
                <div className="menu-icon" onClick={this.handleClick}>
                    <i className={this.state.clicked ? 'fas fa-times' : 'fas fa-bars'}></i>
                </div>
                <ul className={this.state.clicked ? 'nav-menu active': 'nav-menu'}>
                    {MenuItems.map((item,index)=>{
                        return (
                            <li key={index}>
                                <Link className={item.cName} to={item.url}>
                                    {item.title}
                                </Link>
                            </li>
                        )
                    })}
                    
                </ul>
                {this.whatButton()}
            </nav>
        )
    }
}

export default Navbar