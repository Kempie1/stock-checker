////
////  LearningView.swift
////  Stock Checker
////
////  Created by Maximilian Hues on 08.04.21.
////
//
import SwiftUI


struct LearningView: View {
    
    @State public var beginner = 50.0
    @State public var mediumRight = 40.0
    @State public var mediumLeft = 20.0
    @State public var advancedRight = 10.0
    @State public var advancedLeft = 20.0
    @State public var showView = false
    @State public var beginnerLevel = ""
    @State public var mediumRightLevel = ""
    @State public var mediumLeftLevel = ""
    @State public var advancedRightLevel = ""
    @State public var advancedLeftLevel = ""
    @State public var beginnerPressed = false
    @State public var mediumRightPressed = false
    @State public var mediumLeftPressed = false
    @State public var advancedRightPressed = false
    @State public var advancedLeftPressed = false
    var level = ""
    let buttonText = "Start"

    var quizBrain = QuizBrain()

    var body: some View {
        NavigationView {
            ScrollView{
                NavigationLink(destination: LearningViewQuiz(), isActive: $showView) {EmptyView()}
                VStack(spacing: 20) {
                    Spacer()
                    Text("Section 1").font(.system(size: 20))
                    HStack(){
                        ProgressView("Beginner", value: beginner, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    Button(action: {
                            beginner = startButton(level: beginner)
                            beginnerLevel = "Beginner"
                            beginnerPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                    }, label: {
                        Text(buttonText)
                    })
                    
                    
                    
                    Text("Section 2").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Medium", value: mediumRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Medium", value: mediumLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 110){
                        Button(action: {
                                mediumRightLevel = "Medium Lvel 2"
                                mediumRight = startButton(level: mediumRight)
                                mediumRightPressed = true
                                DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                        Button(action: {
                                mediumLeftLevel = "Medium Level 1"
                                mediumLeft = startButton(level: mediumLeft)
                                mediumLeftPressed = true
                                DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                    }
                    
                    
                    
                    Text("Section 3").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Advanced", value: advancedRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Advanced", value: advancedLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 50)
                    {
                        Button(action: {
                            advancedRightLevel = "Advanced 2"
                            advancedRight = startButton(level: advancedRight)
                            advancedRightPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                            
                        }, label: {
                            Text(buttonText)
                        })
                        
                        Button(action: {
                            advancedLeftLevel = "Advanced 1"
                            advancedLeft = startButton(level: advancedLeft)
                            advancedLeftPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                            
                        }, label: {
                            Text(buttonText)
                        })
                        
                    }
                }
            }.navigationBarTitle("Learning View", displayMode: .inline)
        }
    }
    
    func startButton(level: Double)->Double{
        var level = level
        if level < 100 {
            level += 10
        }
        return level
    }
    
    mutating func getLevel()-> String{
        
        if beginnerPressed == true{
            beginner = startButton(level: beginner)
            level = beginnerLevel
        }
        if mediumRightPressed == true{
            level = mediumRightLevel
        }
        if mediumLeftPressed == true{
            level = mediumLeftLevel
        }
        if advancedRightPressed == true{
            level = advancedRightLevel
        }
        if advancedLeftPressed == true{
            level = advancedLeftLevel
        }
        return level
    }

struct LearningView_Previews: PreviewProvider {
    static var previews: some View {
        LearningView()
    }
}

struct CirclerPercentageProgressViewStyle : ProgressViewStyle {
    func makeBody(configuration: LinearProgressViewStyle.Configuration) -> some View {
        VStack(spacing: 10) {
            configuration.label
                .font(.system(size: 13))
                .foregroundColor(Color.secondary)
            ZStack {
                Circle()
                    .stroke(lineWidth: 15.0)
                    .opacity(0.3)
                    .foregroundColor(Color.accentColor.opacity(0.5))
                
                Circle()
                    .trim(from: 0.0, to: CGFloat(configuration.fractionCompleted ?? 0))
                    .stroke(style: StrokeStyle(lineWidth: 15.0, lineCap: .round, lineJoin: .round))
                    .foregroundColor(Color.accentColor)
                
                Text("\(Int((configuration.fractionCompleted ?? 0) * 100))%")
                    .font(.headline)
                    .foregroundColor(Color.secondary)
            }
        } .frame(width: 100, height: 100, alignment: .center)
        .padding()
    }
}

}


