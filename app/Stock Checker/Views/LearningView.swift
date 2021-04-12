////
////  LearningView.swift
////  Stock Checker
////
////  Created by Maximilian Hues on 08.04.21.
////
//
import SwiftUI


struct LearningView: View {
    @State private var beginner = 50.0
    @State private var medium = 20.0
    @State private var advanced = 10.0
    @State public var showView = false

    
    var body: some View {
        NavigationView {
            ScrollView{
                NavigationLink(destination: LearningView2(), isActive: $showView) {EmptyView()}
                VStack(spacing: 20) {
                    Spacer()
                    Text("Section 1").font(.system(size: 20))
                    HStack(){
                        ProgressView("Beginner", value: beginner, total: 100)
                            .font(.system(size: 13))
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                            .frame(width: 100, height: 100, alignment: .center)
                            .padding()
                    }
                    Button(action: {
                        withAnimation {
                            if beginner < 100 {
                                beginner += 10
                            }
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                        }
                    }, label: {
                        Text("Start")
                    })
                    
                    
                    
                    Text("Section 2").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Medium", value: medium, total: 100)
                            .font(.system(size: 13))
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                            .frame(width: 100, height: 100, alignment: .center)
                            .padding()
                        
                        
                        ProgressView("Medium", value: medium, total: 100)
                            .font(.system(size: 13))
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                            .frame(width: 100, height: 100, alignment: .center)
                            .padding()
                    }
                    
                    HStack(spacing: 110){
                        Button(action: {
                            withAnimation {
                                if medium < 100 {
                                    medium += 10
                                }
                                DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                            }
                        }, label: {
                            Text("Start")
                        })
                        Button(action: {
                            withAnimation {
                                if medium < 100 {
                                    medium += 10
                                }
                                DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                            }
                        }, label: {
                            Text("Start")
                        })
                    }
                    
                    
                    
                    Text("Section 3").font(.system(size: 20))
                    HStack(spacing: 10){
                        ProgressView("Advanced", value: advanced, total: 100)
                            .font(.system(size: 13))
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                            .frame(width: 100, height: 100, alignment: .center)
                            .padding()
                        
                        
                        ProgressView("Advanced", value: advanced, total: 100)
                            .font(.system(size: 13))
                            .progressViewStyle(CirclerPercentageProgressViewStyle())
                            .frame(width: 100, height: 100, alignment: .center)
                            .padding()
                        
                    }
                    
                    HStack(spacing: 50)
                    {
                        Button(action: {
                            withAnimation {
                                if advanced < 100 {
                                    advanced += 10
                                }
                            }
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                        }, label: {
                            Text("Start")
                        })
                        
                        Button(action: {
                            withAnimation {
                                if advanced < 100 {
                                    advanced += 10
                                }
                            }
                            DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
                        }, label: {
                            Text("Start")
                        })
                        
                    }
                }
            }.navigationBarTitle("Learning View", displayMode: .inline)
        }
    }
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
        }
    }
}














struct LearningView2: View {
    @State private var buttonColorTrue:Color = .black
    @State private var buttonColorFalse:Color = .black
    
    @State var timer: Timer? = nil
    @State var timerIsPaused: Bool = true
    @State var hours: Int = 0
    @State var minutes: Int = 0
    @State var seconds: Int = 0
    @State var buttonResult = ""
    
    var quizBrain = QuizBrain()
    @State var questionNumber = 0
    var body: some View {
        NavigationView{
            VStack{
                
                
                Text(quizBrain.quiz[questionNumber].text)
                    .font(.system(size: 30))
                
                
                Button(action: {
                    startTimer()
                    buttonResult = "True"
                    anwserButtonPressed(userinput: buttonResult)
                    if buttonResult == quizBrain.quiz[questionNumber].answer{
                        print("Correct")
                        self.buttonColorTrue = .green
                        if self.seconds == 2{
                            self.buttonColorFalse = .black
                            stopTimer()
                        }
                    }
                    else{
                        print("Wrong")
                        self.buttonColorTrue = .red
                        if self.seconds == 2{
                            self.buttonColorFalse = .black
                            stopTimer()
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
                    startTimer()
                    buttonResult = "False"
                    anwserButtonPressed(userinput: buttonResult)
                    if buttonResult == quizBrain.quiz[questionNumber].answer{
                        print("Correct")
                        self.buttonColorFalse = .green
                        if self.seconds == 2{
                            self.buttonColorFalse = .black
                            stopTimer()
                        }
                    }
                    else{
                        print("Wrong")
                        self.buttonColorFalse = .red
                        if self.seconds == 2{
                            self.buttonColorFalse = .black
                            stopTimer()
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

    func startTimer(){
        timerIsPaused = false
        // 1. Make a new timer
        timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true){ tempTimer in
          // 2. Check time to add to H:M:S
          if self.seconds == 59 {
            self.seconds = 0
            if self.minutes == 59 {
              self.minutes = 0
              self.hours = self.hours + 1
            } else {
              self.minutes = self.minutes + 1
            }
          } else {
            self.seconds = self.seconds + 1
          }
            print(self.seconds)
        }
      }

    func stopTimer(){
       timerIsPaused = true
       timer?.invalidate()
       timer = nil
     }

    
func anwserButtonPressed(userinput: String)->Bool{
        var quizBrain = QuizBrain()
        let usersAnwser = userinput
        let result = quizBrain.checkAnwser(usersAnwser)
        return result
    }
}

struct LearningView2_Previews: PreviewProvider {
    static var previews: some View {
        LearningView2()
    }
}
