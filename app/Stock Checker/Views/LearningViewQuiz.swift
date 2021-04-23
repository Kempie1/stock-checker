//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningViewQuiz: View {
    @ObservedObject var vm = QuizViewModel()
    
    var quizBrain = QuizBrain()
    
    //Readable
    @EnvironmentObject var learningViewModel: LearningViewModel
    
    @StateObject var learningQuizViewModel = LearningQuizViewModel()
    
    
//    @State private var buttonColorTrue:Color = Color.black
//    @State private var buttonColorFalse:Color = Color.black
//
//    @State var buttonResultTrue = ""
//    @State var buttonResultFalse = ""
    
//    @State var userIsRight = false
    
//    @State var score = 0
//    @State public var questionNumber = 0
    
//    @State private var showPopUp = false
    
    
    var body: some View {
        NavigationView{
            ZStack(alignment: .center){
                VStack(alignment: .center, spacing: 80){
                    
                    VStack(spacing: 10){
                        Text("Question Number \(learningQuizViewModel.questionNumber)").font(.system(size: 30))
                            .accessibilityIdentifier("questionNumber")
                        
                        Text("Score \(learningQuizViewModel.score)").font(.system(size: 30))
                    }
                    
                    
                    VStack(spacing: 20){
                        Text("Question:").font(.system(size: 30))
                        Text(quizBrain.quiz[learningQuizViewModel.questionNumber].text)
                            .font(.system(size: 30))
                        
                        
                        Button(action: {
                            
                            learningQuizViewModel.buttonResultTrue = "True"
                            if learningQuizViewModel.questionNumber == quizBrain.quiz.count {
                                self.learningQuizViewModel.showPopUp = true
                            }
                            learningQuizViewModel.checkAnwser(input: learningQuizViewModel.buttonResultTrue, questionNumber: learningQuizViewModel.questionNumber)
                            learningQuizViewModel.nextQuestion()
                            learningQuizViewModel.buttonColorTrue = learningQuizViewModel.changeButtonColor(buttonColor: learningQuizViewModel.buttonColorTrue)!
                            
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                                learningQuizViewModel.buttonColorTrue = .black
                            })
                            
                        }){
                            Text("True").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(q: learningQuizViewModel.buttonColorTrue))
                        .accessibility(identifier: "TrueButton")
                        
                        
                        Button(action: {
                            learningQuizViewModel.buttonResultFalse = "False"
                            if learningQuizViewModel.questionNumber == quizBrain.quiz.count {
                                self.learningQuizViewModel.showPopUp = true
                            }
//                            quizViewModel.changeScore()
                            learningQuizViewModel.checkAnwser(input: learningQuizViewModel.buttonResultFalse, questionNumber: learningQuizViewModel.questionNumber)
                            learningQuizViewModel.nextQuestion()
                            learningQuizViewModel.buttonColorFalse = learningQuizViewModel.changeButtonColor(buttonColor: learningQuizViewModel.buttonColorFalse)!
                            
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                                learningQuizViewModel.buttonColorFalse = .black
                            })
                        }){
                            Text("False").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(q: learningQuizViewModel.buttonColorFalse))
                        .accessibility(identifier: "FalseButton")
                        
                        
                        
                    }
                }
                
                if self.learningQuizViewModel.showPopUp == true{
                    
                    ZStack (alignment: .center){
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
                            //                            Button(action: {
                            //                                self.showPopUp = false
                            //                            }, label: {
                            //                                Text("Close")
                            //                            })
                        }.padding()
                    }
                    .frame(width: 360, height: 500)
                    .cornerRadius(20).shadow(radius: 20)
                }
            }
            
        }.environmentObject(learningQuizViewModel)
        
    }
    
//    func getQuestionNumber()->Int{
//        return learningQuizViewModel.questionNumber
//    }
    
//    func getScoreNumber(userIsRight: Bool){
//        var userIsCorrect = userIsRight
//        if userIsCorrect == true{
//            learningQuizViewModel.score += 1
//        }
//    }
    
//    func nextQuestion(){
//        if learningQuizViewModel.questionNumber < quizBrain.quiz.count {
//            learningQuizViewModel.questionNumber += 1
//        }
//        if learningQuizViewModel.questionNumber == quizBrain.quiz.count {
//            self.showPopUp = true
//            learningQuizViewModel.questionNumber = 0
//        }
//    }
    
//    func checkAnwser(input: String, questionNumber: Int)->Bool{
//        if input == quizBrain.quiz[learningQuizViewModel.questionNumber].answer{
//            print("Correct")
//            userIsRight = true
//            learningQuizViewModel.getScoreNumber(userIsRight: userIsRight)
//            return true
//        }
//        else{
//            print("Wrong")
//            userIsRight = false
//            return false
//        }
//    }
    
//    func changeButtonColor(buttonColor: Color) -> Color?{
//        var buttonColor = buttonColor
//        if learningQuizViewModel.userIsRight == true{
//            buttonColor = Color.green
//        }
//
//        if learningQuizViewModel.userIsRight == false{
//            buttonColor = Color.red
//        }
//        return buttonColor
//    }
    
    
    
    
}

struct LearningViewQuiz_Previews: PreviewProvider {
    static var previews: some View {
        LearningViewQuiz(learningQuizViewModel: LearningQuizViewModel())
    }
}


struct AppButtonStyle: ButtonStyle {
    
    let buttonFont = Font.custom("Zilla Slab", size: 20).weight(.bold)
    
    let buttonColor: Color
    
    init(q: Color) {
        self.buttonColor = q
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

