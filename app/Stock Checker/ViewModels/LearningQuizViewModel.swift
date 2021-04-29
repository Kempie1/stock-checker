//
//  LearningQuizViewModel.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 27.04.21.
//

import Foundation
import SwiftUI

class LearningQuizViewModel: ObservableObject{
    @Published var learningQuestions = LearningQuestions()
    
    @Published var score = 0.0
    @Published var questionNumber = 0
    @Published var showPopUp = false
    @Published var userIsRight = false
    @Published var buttonTrueColor:Color = Color.black
    @Published var buttonFalseColor:Color = Color.black
    @Published var buttonTrueResult = ""
    @Published var buttonFalseResult = ""
    @Published var learningQuestionsText = []
    @Published var learningQuestionsAnwsers = []
    
    func checkShowPopUp(){
        if questionNumber == learningQuestions.quiz.count {
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
        if questionNumber < learningQuestions.quiz.count {
            questionNumber += 1
        }
        if questionNumber == learningQuestions.quiz.count {
            self.showPopUp = true
            questionNumber = 0
        }
    }
    
    func checkAnwser(input: String, questionNumber: Int)-> Bool{
        if input == learningQuestions.quiz[questionNumber].answer{
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
    
    func changeButtonTrueColorBackToBlack(){
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
            self.buttonTrueColor = .black
        })
    }
    
    func changeButtonFalseColorBackToBlack(){
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
            self.buttonFalseColor = .black
        })
    }
    
}
