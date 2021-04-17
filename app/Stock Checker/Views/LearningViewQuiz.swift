//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningViewQuiz: View {
    
    var quizBrain = QuizBrain()
    
    @State private var buttonColorTrue:Color = Color.black
    @State private var buttonColorFalse:Color = Color.black
    
    @State var buttonResultTrue = ""
    @State var buttonResultFalse = ""
    
    @State var userIsRight = false
    
    @State var score = 0
    @State public var questionNumber = 0
  
    @State private var showPopUp = false
    
    var body: some View {
        NavigationView{
            ZStack{
                VStack{
                    
                    Text("Question Number \(questionNumber)")
                    //
                    Text("Score \(score)")
                    
                    Text(quizBrain.quiz[questionNumber].text)
                        .font(.system(size: 30))
                    
                    
                    Button(action: {
                        buttonResultTrue = "True"
                        if questionNumber == quizBrain.quiz.count {
                            self.showPopUp = true
                        }
                        checkAnwser(input: buttonResultTrue)
                        nextQuestion()
                        
                        buttonColorTrue = changeButtonColor(buttonColor: buttonColorTrue)!
                        
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                            buttonColorTrue = .black
                        })
                        
                        
                        
                    }){
                        Text("True").font(.system(size: 20))
                    }
                    .buttonStyle(AppButtonStyle(q: buttonColorTrue))
                    
                    
                    Button(action: {
                        buttonResultFalse = "False"
                        if questionNumber == quizBrain.quiz.count {
                            self.showPopUp = true
                        }
                        checkAnwser(input: buttonResultFalse)
                        nextQuestion()
                        
                        buttonColorFalse = changeButtonColor(buttonColor: buttonColorFalse)!
                        
                        
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3, execute: {
                            buttonColorFalse = .black
                        })
                        
                        print(getScore())
                        
                    }){
                        Text("False").font(.system(size: 20))
                    }
                    .buttonStyle(AppButtonStyle(q: buttonColorFalse))
                    
                    
                    
                    
                }
                
                if self.showPopUp == true{
                    ZStack (alignment: .center){
                        Color.white
                        VStack(alignment: .center, spacing: 30) {
                            Text("Congratulations ").foregroundColor(Color.black)
                                .padding(.horizontal, 100)
                                .font(.system(size: 15, weight: .heavy, design: .default))
                            VStack(alignment: .leading, spacing: 10) {
                                Text("Score: \(score)").foregroundColor(Color.black)
                                Text("Level:").foregroundColor(Color.black)
                                Text("You can go back now!").foregroundColor(Color.black)
                                Text("Start with the next level!").foregroundColor(Color.black)
                            }
//                            Button(action: {
//                                self.showPopUp = false
//                            }, label: {
//                                Text("Close")
//                            })
                        }.padding()
                    }
                    .frame(width: 360, height: 250)
                    .cornerRadius(20).shadow(radius: 20)
                }
            }
            
        }
        
    }
    
    
    func nextQuestion(){
        if questionNumber < quizBrain.quiz.count {
            questionNumber += 1
        }
        if questionNumber == quizBrain.quiz.count {
            self.showPopUp = true
            questionNumber = 0
            score = 0
        }
    }
    
    func getScore()->Int{
        return score
    }
    
    func checkAnwser(input: String)->Bool{
        if input == quizBrain.quiz[questionNumber].answer{
            print("Correct")
            userIsRight = true
            score += 1
            return true
        }
        else{
            print("Wrong")
            userIsRight = false
            return false
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
        return buttonColor
    }
    
    
}

struct LearningViewQuiz_Previews: PreviewProvider {
    static var previews: some View {
        LearningViewQuiz()
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

