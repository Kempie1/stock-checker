//
//  LearningStructure.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 12.04.21.
//

import Foundation

struct Questions {
    var text: String
    let answer: String
    
    init(q: String, a: String) {
        self.text = q;
        self.answer = a
    }
}

struct Defintions {
    var text: String
    
    init(d: String) {
        self.text = d;
    }
}
