//
//  ExploreViewTests.swift
//  Stock CheckerUITests
//
//  Created by Valentin Silvera on 23.05.21.
//

import XCTest

@testable import Stock_Checker

class ExploreViewTests: XCTestCase {
    
    var app = XCUIApplication()

    override func setUpWithError() throws {

        continueAfterFailure = false
        app.launch()

    }

    func testSwitchSegments() throws {
        let segmentOne = app.segmentedControls.buttons.element(boundBy: 0)
        let segmentTwo = app.segmentedControls.buttons.element(boundBy: 1)
        let segmentThree = app.segmentedControls.buttons.element(boundBy: 2)
        
        segmentTwo.tap()
        XCTAssertTrue(segmentTwo.isSelected, "Right environment selected");
        XCTAssertTrue(app.staticTexts["Here goes the news"].exists)
        
        segmentThree.tap()
        XCTAssertTrue(segmentThree.isSelected, "Right environment selected");
        XCTAssertTrue(app.staticTexts["Here goes the learning resources"].exists)
        
        segmentOne.tap()
        XCTAssertTrue(segmentOne.isSelected, "Right environment selected");
    }

}
