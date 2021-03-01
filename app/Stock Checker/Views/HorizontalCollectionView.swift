//
//  HorizontalCollectionView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct HorizontalCollectionView: View {
    var body: some View {
        VStack {
            HStack {
                Text("Title")
                    .font(.title)
                
                Spacer()
            }
            
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 20) {
                    ForEach(0..<10) {_ in
                        NavigationLink(destination: StockView()) {
                            RoundedRectangle(cornerRadius: 25.0)
                                .frame(width: 100, height: 100)
                                .foregroundColor(.gray)
                        }
                    }
                }
            }
        }
    }
}

struct HorizontalCollectionView_Previews: PreviewProvider {
    static var previews: some View {
        HorizontalCollectionView()
            .previewLayout(PreviewLayout.sizeThatFits)
            .padding()
            .previewDisplayName("Default preview")
    }
}
