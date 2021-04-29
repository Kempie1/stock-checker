////
////  LearningView.swift
////  Stock Checker
////
////  Created by Maximilian Hues on 08.04.21.
////
//
import SwiftUI


struct LearningView: View {
    
    @EnvironmentObject var learningQuizViewModel: LearningQuizViewModel
    
    @StateObject var learningViewModel = LearningViewModel()
  
    let buttonText = "Start"
    
    var body: some View {
        NavigationView {
            ScrollView(showsIndicators: false) {
                NavigationLink(destination: LearningViewQuiz(), isActive: $learningViewModel.showView) {EmptyView()}
                VStack(spacing: 20) {
                    Spacer()

                    Text("Section 1").font(.system(size: 20))

                    HStack(){
                        ProgressView("Beginner", value: learningViewModel.beginner, total: 100)
                            .progressViewStyle(CircledProgressBar())
                    }

                    Button(action: {
                        learningViewModel.level = "Beginner"
                        learningViewModel.beginnerPressed = true
                        learningViewModel.showQuestionView()
                    }, label: {
                        Text(buttonText)
                    })
                    
                    
                    Text("Section 2").font(.system(size: 20))

                    HStack(spacing: 10) {
                        ProgressView("Medium", value: learningViewModel.mediumRight, total: 100)
                            .progressViewStyle(CircledProgressBar())
                        
                        ProgressView("Medium", value: learningViewModel.mediumLeft, total: 100)
                            .progressViewStyle(CircledProgressBar())
                    }
                    
                    HStack(spacing: 110) {
                        Button(action: {
                            learningViewModel.level = "Medium Lvel 2"
                            learningViewModel.mediumRightPressed = true
                            learningViewModel.showQuestionView()
                        }, label: {
                            Text(buttonText)
                        })
                        Button(action: {
                            learningViewModel.level = "Medium Level 1"
                            learningViewModel.mediumLeftPressed = true
                            learningViewModel.showQuestionView()
                        }, label: {
                            Text(buttonText)
                        })
                    }
                    
                    
                    
                    Text("Section 3").font(.system(size: 20))
                    HStack(spacing: 10) {
                        ProgressView("Advanced", value: learningViewModel.advancedRight, total: 100)
                            .progressViewStyle(CircledProgressBar())
                        
                        ProgressView("Advanced", value: learningViewModel.advancedLeft, total: 100)
                            .progressViewStyle(CircledProgressBar())
                    }
                    
                    HStack(spacing: 110) {
                        Button(action: {
                            learningViewModel.level = "Advanced 2"
                            learningViewModel.advancedRightPressed = true
                            learningViewModel.showQuestionView()
                        }, label: {
                            Text(buttonText)
                        })
                        
                        Button(action: {
                            learningViewModel.level = "Advanced 1"
                            learningViewModel.advancedLeftPressed = true
                            learningViewModel.showQuestionView()
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
        LearningView(learningViewModel: LearningViewModel())
    }
}

struct CircledProgressBar : ProgressViewStyle {
    func makeBody(configuration: LinearProgressViewStyle.Configuration) -> some View {
        VStack(spacing: 10) {
            configuration.label
                .font(.system(size: 15))
                .foregroundColor(Color.black)
            ZStack {
                Circle()
                    .stroke(lineWidth: 15.0)
                    .opacity(0.5)
                    .foregroundColor(Color.gray.opacity(0.5))
                
                Circle()
                    //TRIM is for showing that the circles are not complete yet
                    .trim(from: 0.0, to: CGFloat(configuration.fractionCompleted ?? 0))
                    .stroke(style: StrokeStyle(lineWidth: 15.0, lineCap: .round, lineJoin: .round))
                    .foregroundColor(Color.green)
                
                Text("\(Int((configuration.fractionCompleted ?? 0) * 100))%")
                    .font(.system(size: 16, weight: .medium))
                    .foregroundColor(Color.black)
            }
        } .frame(width: 100, height: 100, alignment: .center)
        .padding()
    }
}


