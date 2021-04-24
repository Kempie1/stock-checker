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
                NavigationLink(destination: LearningViewQuiz(), isActive: $vm.showView) {EmptyView()}
                VStack(spacing: 20) {
                    Spacer()

                    Text("Section 1").font(.system(size: 20)).onAppear(){
                        print(learningQuizViewModel.score)
                        vm.beginner += learningQuizViewModel.score
                        vm.startButton(level: vm.beginner)
                    }

                    HStack(){
                        ProgressView("Beginner", value: vm.beginner, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }

                    Button(action: {
                            vm.beginner = vm.startButton(level: vm.beginner)
                            vm.setLevelBeginner()
                        print(vm.level)
                            vm.beginnerPressed = true
                        DispatchQueue.main.asyncAfter(deadline: .now()) {self.vm.showView = true}
                    }, label: {
                        Text(buttonText)
                    })
                    
                    
                    Text("Section 2").font(.system(size: 20))

                    HStack(spacing: 10){
                        ProgressView("Medium", value: vm.mediumRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Medium", value: vm.mediumLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 110){
                        Button(action: {
                                vm.level = "Medium Lvel 2"
                                vm.mediumRightPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.vm.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                        Button(action: {
                                vm.level = "Medium Level 1"
                                vm.mediumLeftPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.vm.showView = true}
                        }, label: {
                            Text(buttonText)
                        })
                    }
                    
                    
                    
                    Text("Section 3").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Advanced", value: vm.advancedRight, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                        
                        ProgressView("Advanced", value: vm.advancedLeft, total: 100)
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                    }
                    
                    HStack(spacing: 50)
                    {
                        Button(action: {
                            vm.level = "Advanced 2"
                            vm.advancedRightPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.vm.showView = true}
                            
                        }, label: {
                            Text(buttonText)
                        })
                        
                        Button(action: {
                            vm.level = "Advanced 1"
                            vm.advancedLeftPressed = true
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.vm.showView = true}
                            
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


