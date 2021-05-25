//
//  StockCellViewModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import Foundation
import Combine
import SwiftUI

class StockCellViewModel: ObservableObject, Identifiable {
    @Published var stock: Stock
    
    var id: String = ""
    @Published var backgroundColor : Color = Color.green
    
    private var cancellables = Set<AnyCancellable>()
    
    init(stock: Stock) {
        self.stock = stock
        
        $stock
            .compactMap { stock in
                let penultimate = stock.history.penultimate() ?? .nan
                let last = stock.history.last ?? .nan
                
                if penultimate <= last {
                    return Color.green
                } else {
                    return Color.red
                }
            }
            .assign(to: \.backgroundColor, on: self)
            .store(in: &cancellables)
        
        $stock
            .compactMap { $0.id }
            .assign(to: \.id, on: self)
            .store(in: &cancellables)
    }
}
