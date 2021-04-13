//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningView2: View {
    @State private var buttonColorTrue:Color = Color.black
    @State private var buttonColorFalse:Color = Color.black
    
    @State var buttonResultTrue = ""
    @State var buttonResultFalse = ""
    
    @State var userIsRight = false
    
    @State var score = 0
    @State var questionNumber = 0
    
    var quizBrain = QuizBrain()
    
    
    var body: some View {
        
        NavigationView{
            VStack{
                Text("Question Number \(questionNumber)")
                Text("Score \(score)")
                
                Text(quizBrain.quiz[questionNumber].text)
                    .font(.system(size: 30))
                
                Button(action: {
                    buttonResultTrue = "True"
                    checkAnwser(input: buttonResultTrue)
                    buttonColorTrue = changeButtonColor(buttonColor: buttonColorTrue)!
                    print(changeButtonColor(buttonColor: buttonColorFalse))
                    print(buttonColorTrue)
                }){
                    Text("True").font(.system(size: 20))
                }
                .buttonStyle(AppButtonStyle(q: buttonColorTrue))
//                .background(buttonColorTrue)
                
                
                
                Button(action: {
                    buttonResultFalse = "False"
                    checkAnwser(input: buttonResultFalse)
                    buttonColorFalse = changeButtonColor(buttonColor: buttonColorFalse)!
                    print(changeButtonColor(buttonColor: buttonColorFalse))
                }){
                    Text("False").font(.system(size: 20))
                }
                .buttonStyle(AppButtonStyle(q: buttonColorFalse))
//                .background(Color.red)
            }
            
        }
        
    }
    
    
    func checkAnwser(input: String){
        if input == quizBrain.quiz[questionNumber].answer{
            print("Correct")
            userIsRight = true
            questionNumber += 1
            score += 1
        }
        else{
            print("Wrong")
            userIsRight = false
            questionNumber += 1
        }
    }
    
    func changeButtonColor(buttonColor: Color) -> Color?{
        var buttonColor = buttonColor
        if userIsRight == false{
            buttonColor = Color.green
            DispatchQueue.main.asyncAfter(deadline: .now() + 2.0, execute: {
                buttonColor = Color.black
                print("green")
            });return buttonColor
        }
        if userIsRight == true{
            buttonColor = Color.red
            DispatchQueue.main.asyncAfter(deadline: .now() + 2.0, execute: {
                buttonColor = Color.black
                print("red")
            });return buttonColor
        };return Color.black
    }
    
    
    func anwserButtonPressed(userinput: String)->Bool{
        var quizBrain = QuizBrain()
        let usersAnwser = userinput
        let result = quizBrain.checkAnwser(usersAnwser)
        quizBrain.nextQuestion()
        return result
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
