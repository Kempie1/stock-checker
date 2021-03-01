//
//  StockView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI
import SwiftUICharts

struct StockView: View {
    var body: some View {
        Group {
            StockTitleView()
            
            LineView(data: [8,23,54,32,25,37,7,23,12])
            
            StockTextView()
        }
        .padding([.leading, .trailing], 17)
        
        Spacer()
    }
}

struct StockView_Previews: PreviewProvider {
    static var previews: some View {
        StockView()
    }
}
