//
//  ExploreView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct ExploreView: View {
    @State private var selectedPickerIndex = 0
    private let categories = ["Watching", "News", "Learn"]
    
    var body: some View {
        NavigationView{
            ScrollView {

                Picker(selection: $selectedPickerIndex, label: Text("Select feed")) {
                    ForEach(0 ..< categories.count) {
                        Text(self.categories[$0])
                    }
                }
                .pickerStyle(SegmentedPickerStyle())
                .padding([.trailing, .leading], 21)
                
                if selectedPickerIndex == 0 {
                    StocksListView()
                } else if selectedPickerIndex == 1 {
                    Text("Here goes the news")
                } else if selectedPickerIndex == 2 {
                    Text("Here goes the learning resources")
                }
            }
            .fixFlickering()
            .navigationBarTitle(Text("Explore"))
        }
    }
}

struct ExploreView_Previews: PreviewProvider {
    static var previews: some View {
        ExploreView()
    }
}

