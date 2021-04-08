////
////  LearningView.swift
////  Stock Checker
////
////  Created by Maximilian Hues on 08.04.21.
////
//
import SwiftUI

struct LearningView2: View {
    @State private var downloadAmount = 10.0
    var body: some View {
        NavigationView {
            VStack {
                ProgressView("Downloading…", value: downloadAmount, total: 100)
                    .progressViewStyle(CirclerPercentageProgressViewStyle())
                    .frame(width: 120, height: 120, alignment: .center)
                .padding()
                Button(action: {
                    withAnimation {
                        if downloadAmount < 100 {
                            downloadAmount += 10
                        }
                    }
                }, label: {
                    Text("+10%")
                })
            }
            .navigationBarTitle("Learning View", displayMode: .inline)
        }
    }
}

struct LearningView2_Previews: PreviewProvider {
    static var previews: some View {
        LearningView2()
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














struct LearningView: View {
    var body: some View {
            Text("This is just another View")
        }
}

struct LearningView_Previews: PreviewProvider {
    static var previews: some View {
        LearningView()
    }
}
