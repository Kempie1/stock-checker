//
//  StockModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 13.03.21.
//

import Foundation

struct Stock: Identifiable {
    var id = UUID()
    var name: String
    var ticker: String
    var price: Double
    var history: [Double] = [120, 124, 234, 130, 200, 180, 98, 200]
}

var sampleStocks = [
    Stock(name: "Apple", ticker: "AAPL", price: 121.03, history: [119.28, 119.55, 119.55, 119.83, 119.94, 119.46, 119.56, 120.00, 120.00, 120.26, 121.0, 121.03]),
    Stock(name: "Mercado Libre", ticker: "MELI", price: 1550.15),
    Stock(name: "Tesla", ticker: "TSLA", price: 693.73),
    Stock(name: "Beyond Meat", ticker: "BYND", price: 142.45),
    Stock(name: "Walt Disney", ticker: "DIS", price: 197.16),
    Stock(name: "Redfin", ticker: "RDFN", price: 145.06)
]
