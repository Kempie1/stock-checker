//
//  StockCellViewModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import Foundation
import Combine

class StockCellViewModel: ObservableObject, Identifiable {
    @Published var stock: Stock
    
    var id: String = ""
    private var cancellables = Set<AnyCancellable>()
    
    init(stock: Stock) {
        self.stock = stock
        
        $stock
            .map { $0.id }
            .assign(to: \.id, on: self)
            .store(in: &cancellables)
    }
}
