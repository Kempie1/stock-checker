//
//  StockTitleView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct StockTitleView: View {
    var body: some View {
        HStack(alignment:.top) {
            VStack(alignment: .leading) {
                Circle()
                    .frame(width: 50, height: 50)
                    .foregroundColor(.gray)
                Text("Stock Name")
                Text("$val")
                Text("trendfornow")
                    .font(.callout)
                    .foregroundColor(.red)
            }
            .font(.title)
            
            Spacer()
            
            Circle()
                .frame(width: 50, height: 50)
                .foregroundColor(.gray)
        }
    }
}

struct StockTitleView_Previews: PreviewProvider {
    static var previews: some View {
        StockTitleView()
            .previewLayout(PreviewLayout.sizeThatFits)
            .padding()
            .previewDisplayName("Default preview")
    }
}
