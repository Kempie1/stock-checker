//
//  QuestionStructure.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 12.04.21.
//

import Foundation

struct Questions {
    var question: String
    let answer: String
    
    init(q: String, a: String) {
        self.question = q;
        self.answer = a
    }
}
