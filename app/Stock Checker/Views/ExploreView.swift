//
//  ExploreView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct ExploreView: View {
    var body: some View {
        NavigationView{
            VStack {
                HorizontalCollectionView()
                HorizontalCollectionView()
                
                Spacer()
            }
            .navigationBarTitle(Text("Explore"))
            .padding([.leading, .top], 17)
        }
        .redacted(reason: .placeholder)
    }
}

struct ExploreView_Previews: PreviewProvider {
    static var previews: some View {
        ExploreView()
    }
}
