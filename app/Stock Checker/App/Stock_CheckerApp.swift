//
//  Stock_CheckerApp.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 21.02.21.
//

import SwiftUI
import Firebase

@main
struct Stock_CheckerApp: App {
    init() {
        FirebaseApp.configure()
        Auth.auth().signInAnonymously()
      }
    
    var body: some Scene {
        WindowGroup {
            MainView()
        }
    }
}
