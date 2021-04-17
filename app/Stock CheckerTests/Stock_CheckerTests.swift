//
//  Stock_CheckerTests.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 21.02.21.
//

import XCTest
@testable import Stock_Checker

class Stock_CheckerTests: XCTestCase {
    
    var learningView = LearningView()
    var learningViewQuiz = LearningViewQuiz()
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testExample() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual(0, learningViewQuiz.score)
        XCTAssertEqual(0, learningViewQuiz.questionNumber)
        XCTAssertEqual(learningView.beginnerPressed, false)
        XCTAssertEqual(learningView.mediumRightPressed, false)
        XCTAssertEqual(learningView.mediumLeftPressed, false)
        XCTAssertEqual(learningView.advancedRightPressed, false)
        XCTAssertEqual(learningView.advancedLeftPressed, false)
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
