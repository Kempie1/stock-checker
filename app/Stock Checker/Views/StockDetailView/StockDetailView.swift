//
//  StockDetailView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI
import iLineChart

struct StockDetailView: View {
    var stock: Stock
    
    var body: some View {
        Group {
            StockTitleView(stock: stock)
            
            iLineChart(data: stock.history, style: .tertiary, canvasBackgroundColor: Color.clear, displayChartStats: true)
            
            StockTextView()
                .redacted(reason: .placeholder)
        }
        .padding([.leading, .trailing], 17)
        
        Spacer()
    }
}
