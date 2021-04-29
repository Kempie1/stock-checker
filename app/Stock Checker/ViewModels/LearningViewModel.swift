//
//  LearningViewModel.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 21.04.21.
//

import Foundation
import SwiftUI

class LearningViewModel: ObservableObject {
    @Published var level = ""
    @Published var showView = false
    @Published var predictionInterval = 0.2
    //LEVEL FOR LEANRINGVIEW
    @Published var beginner = 50.0
    @Published var mediumRight = 40.0
    @Published var mediumLeft = 20.0
    @Published var advancedRight = 10.0
    @Published var advancedLeft = 20.0
    //LEVEL INIDCATOR
    @Published var beginnerLevel = ""
    @Published var mediumRightLevel = ""
    @Published var mediumLeftLevel = ""
    @Published var advancedRightLevel = ""
    @Published var advancedLeftLevel = ""
    //BUTTON PRESSED
    @Published var beginnerPressed = false
    @Published var mediumRightPressed = false
    @Published var mediumLeftPressed = false
    @Published var advancedRightPressed = false
    @Published var advancedLeftPressed = false
    
    func addScoreToLevel(amount: Double) {
        if beginnerPressed == true {
            beginner += amount
        }
        if mediumLeftPressed == true {
            mediumLeft += amount
        }
        if mediumRightPressed == true {
            mediumRight += amount
        }
        if advancedLeftPressed == true {
            advancedLeft += amount
        }
        if advancedRightPressed == true {
            advancedRight += amount
        }
    }
    
    func showQuestionView() {
        DispatchQueue.main.asyncAfter(deadline: .now()) {self.showView = true}
    }
}
