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
        //Given The Tab Bar is clicked and Start Button
        app.tabBars["Tab Bar"].buttons["Learn"].tap()
        app.scrollViews.otherElements.containing(.staticText, identifier:"Section 1").children(matching: .button).matching(identifier: "Start").element(boundBy: 0).tap()
        
        let trueButton = self.app.buttons["TrueButton"]
        let falseButton = self.app.buttons["FalseButton"]
//        let QuestionNumber = self.app.textFields["questionNumber"]    
        trueButton.tap()
        falseButton.tap()
        trueButton.tap()
        falseButton.tap()
        trueButton.tap()
        falseButton.tap()
        trueButton.tap()
        falseButton.tap()
        trueButton.tap()
        falseButton.tap()
        trueButton.tap()
        falseButton.tap()
        //What should the score be if the button is pressed if it is either false or true for eahc button
        //Assert the percentage calculations
        app.navigationBars.buttons.element(boundBy: 0).tap() //This is the back Button
        //EVERY TEST SHOULD HAVE THAT:
        //OPTIONAL(Given)
        //When
        //Then
        //Assert
        //ACT
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
