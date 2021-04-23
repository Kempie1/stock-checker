////
////  LearningView.swift
////  Stock Checker
////
////  Created by Maximilian Hues on 08.04.21.
////
//
import SwiftUI


struct LearningView: View {

    @ObservedObject var vm = QuizViewModel()
    
    @ObservedObject var learningQuizViewModel: LearningQuizViewModel
    
    @StateObject var learningViewModel = LearningViewModel()
  
    let buttonText = "Start"
    
    var body: some View {
        NavigationView {
            ScrollView{
                NavigationLink(destination: LearningViewQuiz(), isActive: $learningViewModel.showView) {EmptyView()}
                VStack(spacing: 20) {
                    Spacer()

                    Text("Section 1").font(.system(size: 20)).onAppear(){
                        print(learningQuizViewModel.score)
                        learningViewModel.beginner += learningQuizViewModel.score
                    }

                    HStack(){
                        ProgressView("Beginner", value: learningViewModel.beginner, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }

                    Button(action: {
                            learningViewModel.beginner = learningViewModel.startButton(level: learningViewModel.beginner)
                            learningViewModel.level = "Beginner"
                            learningViewModel.beginnerPressed = true
                        DispatchQueue.main.asyncAfter(deadline: .now()) {self.learningViewModel.showView = true}
                    }, label: {
                        Text(buttonText)
                    })
                    
                    
                    Text("Section 2").font(.system(size: 20))

                    HStack(spacing: 10){
                        ProgressView("Medium", value: learningViewModel.mediumRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Medium", value: learningViewModel.mediumLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 110){
                        Button(action: {
                                learningViewModel.level = "Medium Lvel 2"
                                learningViewModel.mediumRightPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.learningViewModel.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                        Button(action: {
                                learningViewModel.level = "Medium Level 1"
                                learningViewModel.mediumLeftPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.learningViewModel.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                    }
                    
                    
                    
                    Text("Section 3").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Advanced", value: learningViewModel.advancedRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Advanced", value: learningViewModel.advancedLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 50)
                    {
                        Button(action: {
                            learningViewModel.level = "Advanced 2"
                            learningViewModel.advancedRightPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.learningViewModel.showView = true}
                            
                        }, label: {
                            Text(buttonText)
                        })
                        
                        Button(action: {
                            learningViewModel.level = "Advanced 1"
                            learningViewModel.advancedLeftPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.learningViewModel.showView = true}
                            
                        }, label: {
                            Text(buttonText)
                        })
                        
                    }
                }
            }.navigationBarTitle("Learning View", displayMode: .inline)
        }.environmentObject(learningViewModel)
    }
    
    
}

struct LearningView_Previews: PreviewProvider {
    static var previews: some View {
        LearningView(learningQuizViewModel: LearningQuizViewModel(), learningViewModel: LearningViewModel())
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


