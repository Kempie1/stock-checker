//
//  StocksListViewModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import Foundation
import Combine
import Resolver

class StocksListViewModel: ObservableObject {
    @Published var stockRepository: StockRepository = Resolver.resolve()
    @Published var stockCellViewModels = [StockCellViewModel]()
    
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        stockRepository.$stocks.map { stocks in
            stocks.map { stock in
                StockCellViewModel(stock: stock)
            }
        }
        .assign(to: \.stockCellViewModels, on: self)
        .store(in: &cancellables)
        print(cancellables)
        print(stockRepository)
    }
}
