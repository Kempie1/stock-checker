//
//  StockRepository.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import Foundation
import Combine
import Resolver
import Disk

class BaseStockRepository {
    @Published var stocks = [Stock]()
}

protocol StockRepository: BaseStockRepository {
    func addStock(_ stock: Stock)
}

class TestDataStockRepository: BaseStockRepository, StockRepository, ObservableObject {
    override init() {
        super.init()
        self.stocks = testDataStock
    }
    
    func addStock(_ stock: Stock) {
        stocks.append(stock)
    }
}
