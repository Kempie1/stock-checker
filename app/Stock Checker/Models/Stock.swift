//
//  StockModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 13.03.21.
//

import Foundation

struct Stocks: Identifiable {
    var id = UUID()
    var name: String
    var ticker: String
    var price: Float
}

var sampleStocks = [
    Stocks(name: "Apple", ticker: "AAPL", price: 121.03),
    Stocks(name: "Mercado Libre", ticker: "MELI", price: 1550.15),
    Stocks(name: "Tesla", ticker: "TSLA", price: 693.73),
    Stocks(name: "Beyond Meat", ticker: "BYND", price: 142.45),
    Stocks(name: "Walt Disney", ticker: "DIS", price: 197.16),
    Stocks(name: "Redfin", ticker: "RDFN", price: 74.61)
]
