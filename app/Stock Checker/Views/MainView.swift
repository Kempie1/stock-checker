//
//  MainView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct MainView: View {
    var body: some View {
        TabView {
            ExploreView()
                .tabItem {
                    Label("Explore", systemImage: "triangle.circle")
                }
            
            LearningView2()
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
