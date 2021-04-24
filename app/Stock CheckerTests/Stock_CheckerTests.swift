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
    var learningViewModel = LearningViewModel()
    var leanringQuizViewModel = LearningQuizViewModel()
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }
    
    func testTrueButton() -> (Bool, Bool){
        //Arrange
        let buttonResultTrue = "True"
        //Act
        //BUTTONTRUE
        var CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 0)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 1)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 2)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 3)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 5)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 7)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 8)
        CheckAnwserReturnTrueButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 11)
        
        var CheckAnwserReturnFalseButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 4)
        CheckAnwserReturnFalseButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 6)
        CheckAnwserReturnFalseButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 9)
        CheckAnwserReturnFalseButtonTrue = leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: 10)
        
        //Assert
        //BUTTONTRUE
        XCTAssertEqual(CheckAnwserReturnTrueButtonTrue, true)
        XCTAssertEqual(CheckAnwserReturnFalseButtonTrue, false)
        
        return (CheckAnwserReturnTrueButtonTrue, CheckAnwserReturnFalseButtonTrue)
        }
    
    func testFalseButton() -> (Bool, Bool){
        let buttonResultFalse = "False"
        
        //BUTTTONFALSE
        var CheckAnwserReturnTrueButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 4)
        CheckAnwserReturnTrueButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 6)
        CheckAnwserReturnTrueButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 9)
        CheckAnwserReturnTrueButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 10)
        
        var CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 0)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 1)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 2)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 3)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 5)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 7)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 8)
        CheckAnwserReturnFalseButtonFalse = leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: 11)
        
        //BUTTTONFALSE
        XCTAssertEqual(CheckAnwserReturnTrueButtonFalse, true)
        XCTAssertEqual(CheckAnwserReturnFalseButtonFalse, false)
        
        return (CheckAnwserReturnTrueButtonFalse, CheckAnwserReturnFalseButtonFalse)
    }
    
    func testScore(){
        var resultTrueButtonAnswerTrue = [] as [Bool]
        var resultTrueButtonAnswerFalse = [] as [Bool]
        
        var resultFalseButtonAnswerTrue = [] as [Bool]
        var resultFalseButtonAnswerFalse = [] as [Bool]
        
        var resultsAllTrueAnswers = [] as [Bool]
        var resultsAllFalseAnswers = [] as [Bool]
        
        let buttonResultFalse = "False"
        let buttonResultTrue = "True"
        var answer = false
        
        
        //Filtering through results of True Button
        for e in 0...11{
            //TRUE BUTTON
            if leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: e) == true{
                resultTrueButtonAnswerTrue.append(leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: e))
                print(e)
            
                print(Int(leanringQuizViewModel.score))
                XCTAssert(Int(leanringQuizViewModel.score), 5)
                XCTAssert(Int(leanringQuizViewModel.score), 7)
                XCTAssert(Int(leanringQuizViewModel.score), 8)
                XCTAssert(Int(leanringQuizViewModel.score), 0)
                XCTAssert(Int(leanringQuizViewModel.score), Int(11))
                XCTAssert(Int(leanringQuizViewModel.score), 1)
                XCTAssert(Int(leanringQuizViewModel.score), 2)
                XCTAssert(Int(leanringQuizViewModel.score), 3)
            
            }
            
            //FALSE BUTTON
            if leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: e) == true{
                resultTrueButtonAnswerTrue.append(leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: e))
                //When all Anwseres are correct
            }
            

        }
        resultsAllTrueAnswers = resultTrueButtonAnswerTrue + resultTrueButtonAnswerTrue
        
        
        
        
        for e in 0...11{
            if leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: e) == false{
                resultFalseButtonAnswerTrue.append(leanringQuizViewModel.checkAnwser(input: buttonResultTrue,questionNumber: e))
                //When all Anwseres are Wrong
                XCTAssertEqual(Int(leanringQuizViewModel.score), 0)
            }
            if leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: e) == false{
                resultFalseButtonAnswerFalse.append(leanringQuizViewModel.checkAnwser(input: buttonResultFalse,questionNumber: e))
                //When all Anwseres are Wrong
                XCTAssertEqual(Int(leanringQuizViewModel.score), 0)
            }
            
        }
        resultsAllFalseAnswers = resultFalseButtonAnswerTrue + resultFalseButtonAnswerFalse
        
        for i in 0...11{
            
        }
        
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
