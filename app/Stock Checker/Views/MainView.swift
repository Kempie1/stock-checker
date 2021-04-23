//
//  MainView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

//State is a state that is depending on state data so what state the app is in

struct MainView: View {

    var body: some View {        
        TabView {
            ExploreView()
                .tabItem {
                    Label("Explore", systemImage: "triangle.circle")
                }
            
            LearningView(learningQuizViewModel: LearningQuizViewModel(), learningViewModel: LearningViewModel())
                .tabItem {
                    Label("Learn", systemImage: "book.circle")
                }
            
            AccountView()
                .tabItem {
                    Label("Profile", systemImage: "person.crop.circle")
                }
        }
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}
