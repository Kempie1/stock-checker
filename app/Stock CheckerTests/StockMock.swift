//
//  StockMock.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 23.05.21.
//

import Foundation
@testable import Stock_Checker

let allRedStocks : [Stock] = [
    Stock(name: "Stock 1", ticker: "1", price: 50, history: [50, 49, 48, 47, 46]),
    Stock(name: "Stock 2", ticker: "2", price: 40, history: [40, 39, 38, 37, 36]),
    Stock(name: "Stock 3", ticker: "3", price: 30, history: [30, 29, 28, 27, 26])
]

let allGreenStocks : [Stock] = [
    Stock(name: "Stock 1", ticker: "1", price: 50, history: [50, 51, 52, 53, 54]),
    Stock(name: "Stock 2", ticker: "2", price: 40, history: [40, 41, 42, 43, 44]),
    Stock(name: "Stock 3", ticker: "3", price: 30, history: [30, 31, 32, 33, 34])
]
