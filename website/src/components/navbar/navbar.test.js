import React from "react"
import Navbar from "./navbar"
import { render } from '@testing-library/react';
import TestRenderer from 'react-test-renderer';
import { BrowserRouter as Router, Link} from "react-router-dom"


test("<Navbar/> doesn't crash", ()=>{
    const div = document.createElement("div");
    render (<Router><Navbar/></Router>,div)
})

test("<Navbar/> matches snapshot", ()=>{
    const renderedComponent = TestRenderer.create(<Router><Navbar/></Router>)
    expect(renderedComponent).toMatchSnapshot()
})








/*whatButton = () =>{
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
    }*/