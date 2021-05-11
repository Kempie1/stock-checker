import React from "react"
import Button from "./button"
import { render } from '@testing-library/react';
import TestRenderer from 'react-test-renderer';


test("<Button/> doesn't crash", ()=>{
    const div = document.createElement("div");
    render (<Button>test</Button>,div)
})

test("<Button/> matches snapshot", ()=>{
    const renderedComponent = TestRenderer.create(<Button>test</Button>)
    expect(renderedComponent).toMatchSnapshot()
})