//
//  StocksListView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import SwiftUI
import iLineChart

struct StocksListView: View {
    @ObservedObject var stockListVM = StocksListViewModel()
    
    var body: some View {
        VStack(alignment: .leading) {
            ForEach(stockListVM.stockCellViewModels) { stockCellVM in
                NavigationLink(destination: StockDetailView(stock: stockCellVM.stock)) {
                    StockCell(stockCellVM: stockCellVM)
                }
            }
        }
    }
}

struct StockCell: View {
    @ObservedObject var stockCellVM: StockCellViewModel
    
    var body: some View {
        HStack(spacing: 15){
            VStack{
                HStack{
                    VStack(alignment: .leading, spacing: 5) {
                        
                        Text(stockCellVM.stock.name)
                            .font(.title2)
                            .foregroundColor(.primary)
                        
                        Text(stockCellVM.stock.ticker)
                            .font(.caption)
                            .foregroundColor(.gray)
                    }
                    
                    Spacer()
                    
                    ZStack {
                        RoundedRectangle(cornerRadius: 8)
                            .fill(stockCellVM.backgroundColor)
                            .frame(width: 100, height: 50)
                        Text(String(stockCellVM.stock.price))
                            .foregroundColor(.white)
                    }
                }
                Divider()
            }
        }
        .padding(.horizontal)
    }
}

enum InputError: Error {
    case empty
}
