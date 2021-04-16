//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningView2: View {
    
    var quizBrain = QuizBrain()
    var learningView = LearningView()
    
    @State private var buttonColorTrue:Color = Color.black
    @State private var buttonColorFalse:Color = Color.black
    
    @State var buttonResultTrue = ""
    @State var buttonResultFalse = ""
    
    @State var userIsRight = false
    
    @State var score = 0
    @State public var questionNumber = 0
    
    @State var level = ""
    
    let variable = LearningView()
    
    var body: some View {
        
        NavigationView{
            VStack{
                Text("Question Number \(questionNumber)")
                    .onAppear {
                    level = self.variable.levelDecision()
                    print(level)
                }
                Text("Score \(score)")
                
                Text(level)
                    .font(.system(size: 30))
                    
                
                Button(action: {
                    buttonResultTrue = "True"
                    nextQuestion()
                    checkAnwser(input: buttonResultTrue)
                    buttonColorTrue = changeButtonColor(buttonColor: buttonColorTrue)!
                    print(changeButtonColor(buttonColor: buttonColorFalse))
                    print(buttonColorTrue)
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                        buttonColorTrue = .black
                    })

                }){
                    Text("True").font(.system(size: 20))
                }
                .buttonStyle(AppButtonStyle(q: buttonColorTrue))
                
                
                Button(action: {
                    buttonResultFalse = "False"
                    nextQuestion()
                    checkAnwser(input: buttonResultFalse)
                    buttonColorFalse = changeButtonColor(buttonColor: buttonColorFalse)!
                    print(changeButtonColor(buttonColor: buttonColorFalse))
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                        buttonColorFalse = .black
                    })

                }){
                    Text("False").font(.system(size: 20))
                }
                .buttonStyle(AppButtonStyle(q: buttonColorFalse))
            }
            
        }
        
    }
    
    func nextQuestion(){
        if questionNumber < quizBrain.quiz.count {
            questionNumber += 1
        }
        if questionNumber == quizBrain.quiz.count {
            questionNumber = 0
            score = 0
        }
    }
    
    func checkAnwser(input: String){
        if input == quizBrain.quiz[questionNumber].answer{
            print("Correct")
            userIsRight = true
            score += 1
        }
        else{
            print("Wrong")
            userIsRight = false
        }
    }
    
    func changeButtonColor(buttonColor: Color) -> Color?{
        var buttonColor = buttonColor
        if userIsRight == false{
            buttonColor = Color.green
            
        }
        
        if userIsRight == true{
            buttonColor = Color.red
        }
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0, execute: {
            buttonColor = Color.black
        })
        return buttonColor
    }
    

}

struct LearningView2_Previews: PreviewProvider {
    static var previews: some View {
        LearningView2()
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
