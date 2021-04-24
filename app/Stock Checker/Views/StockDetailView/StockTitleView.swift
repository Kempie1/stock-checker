//
//  StockTitleView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct StockTitleView: View {
    var stock: Stock
    
    var body: some View {
        HStack(alignment:.top) {
            VStack(alignment: .leading) {
                Circle()
                    .frame(width: 50, height: 50)
                    .foregroundColor(.gray)
                Text(stock.name)
                    .font(.title)
                Text(stock.ticker)
                    .font(.callout)
                Text("↗$1.3560(0.12%)")
                    .font(.callout)
                    .foregroundColor(.green)
            }
            .font(.title)
            
            Spacer()
            
            Circle()
                .frame(width: 50, height: 50)
                .foregroundColor(.gray)
        }
    }
}
