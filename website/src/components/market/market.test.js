import React from "react"
import { render } from '@testing-library/react';
import {Market, gainOrLoss, differenceArrow, getAvailable, makeBlocks} from "./market"
import { BrowserRouter as Router, Link} from "react-router-dom"
import TestRenderer from 'react-test-renderer';

const axios = require('axios')
jest.mock('axios')
const data = require('../../mocks/available.json');



test("gainOrLoss", ()=>{
    expect(gainOrLoss(10,3)).toBe("loss")
    expect(gainOrLoss(3,10)).toBe("gain")
    expect(gainOrLoss(10,10)).toBe("same")
})

test("differenceArrow", ()=>{
    expect(differenceArrow(10,3)).toBe("fa-arrow-down")
    expect(differenceArrow(3,10)).toBe("fa-arrow-up")
    expect(differenceArrow(10,10)).toBe("fa-equals")
})

test("makeBlocks matches snapshot", ()=>{
    const mockblock=["A", "Agilent Technologies, Inc.", "264724", "132.31", "131.3"]
    const component = render (
    <Router>
        {makeBlocks(mockblock)}
    </Router>
    )
    expect(component.container).toMatchSnapshot();
})

test("<Market/> doesn't crash", ()=>{
    const div = document.createElement("div");
    render (<Market test={true} tickers={data} />,div)
})


test ("mock api call getavailable", ()=>{
    //arange
    const mockedResponse = data
    axios.get.mockResolvedValue(mockedResponse)
    const marke = require ('./market')
    //act
    marke.getAvailable()
    //asserts
    expect(axios.get).toHaveBeenCalled()
    expect(axios.get).toHaveBeenCalledWith(`https://stockcheckerdb.herokuapp.com/getavailable/`)

})

test("<Market/> matches snapshot", ()=>{
    const renderedComponent = TestRenderer.create(<Market test={true}  tickers={data} />)
    expect(renderedComponent).toMatchSnapshot()

})

