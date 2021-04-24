//
//  QuizBrainModel.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 21.04.21.
//

import Foundation
import SwiftUI

class LearningViewModel: ObservableObject{
    @Published var level = ""
    @Published var showView = false
    @Published var predictionInterval = 0.2
    //LEVEL FOR LEANRINGVIEW
    @Published var beginner = 50.0
    @Published var mediumRight = 40.0
    @Published var mediumLeft = 20.0
    @Published var advancedRight = 10.0
    @Published var advancedLeft = 20.0
    //LEVEL INIDCATOR
    @Published var beginnerLevel = ""
    @Published var mediumRightLevel = ""
    @Published var mediumLeftLevel = ""
    @Published var advancedRightLevel = ""
    @Published var advancedLeftLevel = ""
    //BUTTON PRESSED
    @Published var beginnerPressed = false
    @Published var mediumRightPressed = false
    @Published var mediumLeftPressed = false
    @Published var advancedRightPressed = false
    @Published var advancedLeftPressed = false
    
    func addScoreToLevel(amount: Double) {
        if beginnerPressed == true{
            beginner += amount
        }
        if mediumLeftPressed == true{
            mediumLeft += amount
        }
        if mediumRightPressed == true{
            mediumRight += amount
        }
        if advancedLeftPressed == true{
            advancedLeft += amount
        }
        if advancedRightPressed == true{
            advancedRight += amount
        }
    }
    
    
}

class LearningQuizViewModel: ObservableObject{
    @Published var quizBrain = QuizBrain()
    
    @Published var score = 0.0
    @Published var questionNumber = 0
    @Published var showPopUp = false
    @Published var userIsRight = false
    @Published var buttonColorTrue:Color = Color.black
    @Published var buttonColorFalse:Color = Color.black
    @Published var buttonResultTrue = ""
    @Published var buttonResultFalse = ""
    @Published var quizBrainText = []
    @Published var quizBrainAnwsers = []
    
    func checkShowPopUp(){
        if questionNumber == quizBrain.quiz.count {
            self.showPopUp = true
        }
    }
    
    func getScoreNumber(userIsRight: Bool){
        let userIsCorrect = userIsRight
        if userIsCorrect == true{
            score += 1
        }
    }
    
    func nextQuestion(){
        if questionNumber < quizBrain.quiz.count {
            questionNumber += 1
        }
        if questionNumber == quizBrain.quiz.count {
            self.showPopUp = true
            questionNumber = 0
        }
    }
    
    func checkAnwser(input: String, questionNumber: Int)-> Bool{
        if input == quizBrain.quiz[questionNumber].answer{
            userIsRight = true
            getScoreNumber(userIsRight: userIsRight)
            return true
        }
        else{
            userIsRight = false
            return false
        }
    }
    
    func changeButtonColor(buttonColor: Color) -> Color?{
        var buttonColor = buttonColor
        if userIsRight == true{
            buttonColor = Color.green
        }
        
        if userIsRight == false{
            buttonColor = Color.red
        }
        return buttonColor
    }
    
}
