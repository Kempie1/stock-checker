//
//  Stock_CheckerUITests.swift
//  Stock CheckerUITests
//
//  Created by Valentin Silvera on 21.02.21.
//

import XCTest

class Stock_CheckerUITests: XCTestCase {
    
    private var app: XCUIApplication!

    override func setUp(){
        super.setUp()
        self.app = XCUIApplication()
        self.app.launch()
    }
    
    func testLearningViewQuizSucess(){
        app.tabBars["Tab Bar"].buttons["Learn"].tap()
        app.scrollViews.otherElements.containing(.staticText, identifier:"Section 1").children(matching: .button).matching(identifier: "Start").element(boundBy: 0).tap()
        let TrueButton = self.app.buttons["TrueButton"]
        let FalseButton = self.app.buttons["FalseButton"]
        TrueButton.tap()
        FalseButton.tap()
        TrueButton.tap()
        FalseButton.tap()
        TrueButton.tap()
        FalseButton.tap()
        TrueButton.tap()
        FalseButton.tap()
        TrueButton.tap()
        FalseButton.tap()
        TrueButton.tap()
        FalseButton.tap()
        app.navigationBars.buttons.element(boundBy: 0).tap() //This is the back Button
    }

    func testLaunchPerformance() throws {
        if #available(macOS 10.15, iOS 13.0, tvOS 13.0, *) {
            // This measures how long it takes to launch your application.
            measure(metrics: [XCTApplicationLaunchMetric()]) {
                XCUIApplication().launch()
            }
        }
    }
}
