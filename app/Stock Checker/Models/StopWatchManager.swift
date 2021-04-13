//
//  StopWatchManager.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 13.04.21.
//

import Foundation

class StopWatchManager: ObservableObject{
    @Published var secondsElapsed = 0.0
    @Published var mode: stopWatchMode = .stopped
    var timer = Timer()
    
    func start() {
            mode = .running
            timer = Timer.scheduledTimer(withTimeInterval: 0.1, repeats: true) { timer in
                self.secondsElapsed += 0.1
            }
        }
    func stop() {
            timer.invalidate()
            secondsElapsed = 0
            mode = .stopped
        }
}

enum stopWatchMode {
    case running
    case stopped
    case paused
}
