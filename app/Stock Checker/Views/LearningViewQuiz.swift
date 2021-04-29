//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningViewQuiz: View {
    
    @EnvironmentObject var learningViewModel: LearningViewModel
    
    @StateObject var learningQuizViewModel = LearningQuizViewModel()
    
    var body: some View {
        NavigationView {
            ZStack(alignment: .center) {
                VStack(alignment: .center, spacing: 80) {
                    
                    VStack(spacing: 10) {
                        Text("Question Number \(learningQuizViewModel.questionNumber)")
                            .font(.system(size: 30))
                            .accessibilityIdentifier("questionNumber")
                        
                        Text("Score \(learningQuizViewModel.score)").font(.system(size: 30))
                            .accessibilityIdentifier("scoreNumber")
                    }
                    
                    
                    VStack(spacing: 30){
                        Text("Question:").font(.system(size: 30))
                        
                        Text(learningQuizViewModel.learningQuestions.quiz[learningQuizViewModel.questionNumber].question)
                            .font(.system(size: 30))
                    }
                    
                    
                    VStack(spacing: 20) {
                        Button(action: {
                            learningQuizViewModel.buttonTrueResult = "True"
                            learningQuizViewModel.checkShowPopUp()
                            
                            _ = learningQuizViewModel.checkAnwser(input: learningQuizViewModel.buttonTrueResult, questionNumber: learningQuizViewModel.questionNumber)
                            
                            learningQuizViewModel.nextQuestion()
                            
                            learningQuizViewModel.buttonTrueColor = learningQuizViewModel.changeButtonColor(buttonColor: learningQuizViewModel.buttonTrueColor)!
                            
                            learningQuizViewModel.changeButtonTrueColorBackToBlack()
                            
                        }){
                            Text("True").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(buttonColor: learningQuizViewModel.buttonTrueColor))
                        .accessibility(identifier: "trueButton")
                        
                        
                        Button(action: {
                            learningQuizViewModel.buttonFalseResult = "False"
                            learningQuizViewModel.checkShowPopUp()
                            
                            _ = learningQuizViewModel.checkAnwser(input: learningQuizViewModel.buttonFalseResult, questionNumber: learningQuizViewModel.questionNumber)
                            
                            learningQuizViewModel.nextQuestion()
                            
                            learningQuizViewModel.buttonFalseColor = learningQuizViewModel.changeButtonColor(buttonColor: learningQuizViewModel.buttonFalseColor)!
                            
                            learningQuizViewModel.changeButtonFalseColorBackToBlack()
                        }){
                            Text("False").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(buttonColor: learningQuizViewModel.buttonFalseColor))
                        .accessibility(identifier: "falseButton")
                    }
                }
                
                if self.learningQuizViewModel.showPopUp == true {
                    
                    ZStack (alignment: .center) {
                        Color.white
                        VStack(alignment: .center, spacing: 30) {
                            Text("Congratulations ")
                                .foregroundColor(Color.black)
                                .font(.system(size: 25, weight: .heavy,design: .default))
                            VStack(alignment: .leading, spacing: 10) {
                                Text("Score: \(learningQuizViewModel.score)")
                                    .foregroundColor(Color.black)
                                    .font(.system(size: 20, design: .default))
                                Text("Level: \(learningViewModel.level)")
                                    .foregroundColor(Color.black)
                                    .font(.system(size: 20, design: .default))
                                Text("You can go back now!")
                                    .foregroundColor(Color.black)
                                    .font(.system(size: 20, design: .default))
                                Text("Start with the next level!")
                                    .foregroundColor(Color.black)
                                    .font(.system(size: 20, design: .default))
                            }
                        }.padding()
                    }
                    .onAppear {
                        learningViewModel.addScoreToLevel(amount: learningQuizViewModel.score)
                    }
                    .frame(width: 360, height: 500)
                    .cornerRadius(20).shadow(radius: 20)
                }
            }
            
        }.environmentObject(learningQuizViewModel)
        
    }
}

struct LearningViewQuiz_Previews: PreviewProvider {
    static var previews: some View {
        LearningViewQuiz(learningQuizViewModel: LearningQuizViewModel())
    }
}


struct AppButtonStyle: ButtonStyle {
    
    let buttonFont = Font.custom("Zilla Slab", size: 20).weight(.bold)
    
    let buttonColor: Color
    
    init(buttonColor: Color) {
        self.buttonColor = buttonColor
    }
    
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration
            .label
            .font(buttonFont)
            .foregroundColor(.orange)
            .padding(.all)
            .background(buttonColor)
            .cornerRadius(16)
    }
}

