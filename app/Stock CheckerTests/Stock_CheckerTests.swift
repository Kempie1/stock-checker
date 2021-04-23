//
//  Stock_CheckerTests.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 21.02.21.
//

import XCTest
@testable import Stock_Checker

class Stock_CheckerTests: XCTestCase {
    
    var learningView = LearningView(learningQuizViewModel: LearningQuizViewModel())
    var learningViewQuiz = LearningViewQuiz()
    var quizBrain = QuizBrain()
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

//    func testExample() throws {
//        // This is an example of a functional test case.
//        // Use XCTAssert and related functions to verify your tests produce the correct results.
//        XCTAssertEqual(0, learningViewQuiz.score)
//        XCTAssertEqual(0, learningViewQuiz.questionNumber)
//        XCTAssertEqual(learningView.beginnerPressed, false)
//        XCTAssertEqual(learningView.mediumRightPressed, false)
//        XCTAssertEqual(learningView.mediumLeftPressed, false)
//        XCTAssertEqual(learningView.advancedRightPressed, false)
//        XCTAssertEqual(learningView.advancedLeftPressed, false)
//        //Pick some fucntions that I want to test
//        //Look at the aritcle send on slack
//        //do enD to end test
//        //I should cover every single possible failing case in order to find an error quikly remeber the 1+1 = or 1+1 = 3 its not going to fail but it is wrong
////        for each otpion there will be 4 test 2 test for true and 2 test for false
//
//    }
    
    func testCheckanwserbuttons(){
        //Arrange
        let buttonResultTrue = "True"
        let buttonResultFalse = "False"
        var checkScore: Int = 0
        
        //Act
        
        //BUTTONTRUE
        var CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 0)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 1)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 2)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 3)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 5)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 7)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 8)
        CheckAnwserReturnTrueButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 11)
        
        var CheckAnwserReturnFalseButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 4)
        CheckAnwserReturnFalseButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 6)
        CheckAnwserReturnFalseButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 9)
        CheckAnwserReturnFalseButtonTrue = learningViewQuiz.checkAnwser(input: buttonResultTrue,questionNumber: 10)
        
        //BUTTTONFALSE
        var CheckAnwserReturnTrueButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 4)
        CheckAnwserReturnTrueButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 6)
        CheckAnwserReturnTrueButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 9)
        CheckAnwserReturnTrueButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 10)
        
        var CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 0)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 1)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 2)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 3)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 5)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 7)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 8)
        CheckAnwserReturnFalseButtonFalse = learningViewQuiz.checkAnwser(input: buttonResultFalse,questionNumber: 11)
        
        //Assert
        //BUTTONTRUE
        XCTAssertEqual(CheckAnwserReturnTrueButtonTrue, true)
        //XCTAssertEqual(CheckAnwserReturnFalseButtonTrue, false)
        
        //BUTTTONFALSE
        //XCTAssertEqual(CheckAnwserReturnTrueButtonFalse, true)
        XCTAssertEqual(CheckAnwserReturnFalseButtonFalse, false)
        }
    
//    func testCheckScore(){
//        //Arrange
//        let userIsRightTrue = true
//        let userIsRightFalse = false
//
//        //Act
//        let checkUserIsRightTrue = learningViewQuiz.getScoreNumber(userIsRight: userIsRightTrue)
//
//        let checkUserIsRightFalse = learningViewQuiz.getScoreNumber(userIsRight: userIsRightFalse)
//
//        //Assert
//        XCTAssertEqual(checkUserIsRightTrue,0)
//        XCTAssertEqual(checkUserIsRightFalse,0)
//    }
    

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
