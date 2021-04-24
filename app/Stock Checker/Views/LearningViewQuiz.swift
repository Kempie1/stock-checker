//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningViewQuiz: View {
    @ObservedObject var vm = QuizViewModel()

    //Readable
    @EnvironmentObject var learningViewModel: LearningViewModel
    
    @StateObject var learningQuizViewModel = LearningQuizViewModel()
    
    var body: some View {
        NavigationView{
            ZStack(alignment: .center){
                VStack(alignment: .center, spacing: 80){
                    
                    VStack(spacing: 10){
                        Text("Question Number \(vm.questionNumber)").font(.system(size: 30))
                            .accessibilityIdentifier("questionNumber")
                        
                        Text("Score \(vm.score)").font(.system(size: 30))
                    }
                    
                    
                    VStack(spacing: 20){
                        Text("Question:").font(.system(size: 30))
                        Text(vm.quizBrain.quiz[vm.questionNumber].text)
                            .font(.system(size: 30))
                        
                        
                        Button(action: {
                            
                            vm.buttonResultTrue = "True"
                            if vm.questionNumber == vm.quizBrain.quiz.count {
                                self.vm.showPopUp = true
                            }
                            vm.checkAnwser(input: vm.buttonResultTrue, questionNumber: vm.questionNumber)
                            vm.nextQuestion()
                            vm.buttonColorTrue = vm.changeButtonColor(buttonColor: vm.buttonColorTrue)!
                            
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                                vm.buttonColorTrue = .black
                            })
                            
                        }){
                            Text("True").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(q: vm.buttonColorTrue))
                        .accessibility(identifier: "TrueButton")
                        
                        
                        Button(action: {
                            vm.buttonResultFalse = "False"
                            if vm.questionNumber == vm.quizBrain.quiz.count {
                                self.vm.showPopUp = true
                            }
                            vm.checkAnwser(input: vm.buttonResultFalse, questionNumber: vm.questionNumber)
                            vm.nextQuestion()
                            vm.buttonColorFalse = vm.changeButtonColor(buttonColor: vm.buttonColorFalse)!
                            
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                                vm.buttonColorFalse = .black
                            })
                        }){
                            Text("False").font(.system(size: 20))
                        }
                        .buttonStyle(AppButtonStyle(q: vm.buttonColorFalse))
                        .accessibility(identifier: "FalseButton")
                    }
                }
                
                if self.vm.showPopUp == true{
                    
                    ZStack (alignment: .center){
                        Color.white
                        VStack(alignment: .center, spacing: 30) {
                            Text("Congratulations ")
                                .foregroundColor(Color.black)
                                .font(.system(size: 25, weight: .heavy,design: .default))
                            VStack(alignment: .leading, spacing: 10) {
                                Text("Score: \(vm.score)")
                                    .foregroundColor(Color.black)
                                    .font(.system(size: 20, design: .default))
                                Text("Level: \(vm.level)")
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

