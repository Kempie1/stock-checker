//
//  LearningViewQuiz.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import SwiftUI

struct LearningView2: View {
    @State private var buttonColorTrue:Color = .black
    @State private var buttonColorFalse:Color = .black
    
    @State var buttonResult = ""
    
    var quizBrain = QuizBrain()
    @ObservedObject var stopWatchManager = StopWatchManager()
    
    @State var questionNumber = 0
    
    var body: some View {
        
        NavigationView{
            VStack{
                
                
                Text(quizBrain.quiz[questionNumber].text)
                    .font(.system(size: 30))
                
                
                Button(action: {
                    buttonResult = "True"
                    anwserButtonPressed(userinput: buttonResult)
                    if buttonResult == quizBrain.quiz[questionNumber].answer{
                        print("Correct")
                        self.buttonColorTrue = .green
                        
                        if stopWatchManager.secondsElapsed > 2{
                            self.buttonColorFalse = .black

                        }
                    }
                    else{
                        print("Wrong")
                        self.buttonColorTrue = .red
                        if stopWatchManager.secondsElapsed > 2{
                            self.buttonColorFalse = .black
                        }
                    }
                    questionNumber += 1
                }){
                    Text("True").font(.system(size: 20))
                }
                .foregroundColor(.orange)
                .padding(.all)
                .background(buttonColorTrue)
                .cornerRadius(16)
                
                
                
                Button(action: {
                    
                    buttonResult = "False"
                    anwserButtonPressed(userinput: buttonResult)
                    if buttonResult == quizBrain.quiz[questionNumber].answer{
                        print("Correct")
                        self.buttonColorFalse = .green
                        if stopWatchManager.secondsElapsed > 2{
                            self.buttonColorFalse = .black
                        }
                    }
                    else{
                        print("Wrong")
                        self.buttonColorFalse = .red
                        if stopWatchManager.secondsElapsed > 2{
                            
                            self.buttonColorFalse = .black
                        }
                    }
                    questionNumber += 1
                }){
                    Text("False").font(.system(size: 20))
                }
                .foregroundColor(.orange)
                .padding(.all)
                .background(buttonColorFalse)
                .cornerRadius(16)
            }
            
            }
        
        }

    

    
func anwserButtonPressed(userinput: String)->Bool{
        var quizBrain = QuizBrain()
        let usersAnwser = userinput
        let result = quizBrain.checkAnwser(usersAnwser)
        stopWatchManager.start()
        print(stopWatchManager.secondsElapsed)
        return result
    }

    
    
}

struct LearningView2_Previews: PreviewProvider {
    static var previews: some View {
        LearningView2()
    }
}
 
