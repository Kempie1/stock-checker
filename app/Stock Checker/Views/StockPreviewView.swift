//
//  StockPreviewView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 13.03.21.
//

import SwiftUI
import iLineChart

struct StockPreviewView: View {
    var stock: Stock
    
    var body: some View {
        
        HStack(spacing: 15){
            
            VStack{
                
                HStack{
                    
                    VStack(alignment: .leading, spacing: 5) {
                        
                        Text(stock.name)
                            .font(.title2)
                            .foregroundColor(.primary)
                        
                        Text(stock.ticker)
                            .font(.caption)
                            .foregroundColor(.gray)
                    }
                    
                    Spacer()
                    
                    //TODO: Create my own preview chart
                    iLineChart(
                        data: stock.history,
                        style: .tertiary,
                        canvasBackgroundColor: Color.clear,
                        curvedLines: false
                    )
                    .frame(maxWidth: 100, maxHeight: 60)
                    .padding(.trailing, 16)
                    
                    ZStack {
                        RoundedRectangle(cornerRadius: 8)
                            .fill(Color.green)
                            .frame(width: 100, height: 50)
                        Text(String(stock.price))
                            .foregroundColor(.white)
                    }
                }
                
                Divider()
            }
        }
        .padding(.horizontal)
    }
}
