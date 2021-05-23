//
//  StockModel.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 13.03.21.
//

import Foundation

struct Stock: Identifiable {
    var id = UUID().uuidString
    var name: String
    var ticker: String
    var price: Double
    var history: [Double] = [120, 124, 234, 130, 200, 180, 98, 200]
}

#if DEBUG
let testDataStock = [
    Stock(name: "Apple", ticker: "AAPL", price: 121.03, history: [119.28, 119.55, 119.55, 119.83, 119.94, 119.46, 119.56, 120.00, 120.00, 120.26, 123.0, 121.03]),
    Stock(name: "Mercado Libre", ticker: "MELI", price: 50.0, history: [50, 49, 48, 47, 46]),
    Stock(name: "Tesla", ticker: "TSLA", price: 50.0, history: [50, 51, 52, 53, 54]),
    Stock(name: "Beyond Meat", ticker: "BYND", price: 142.45),
    Stock(name: "Walt Disney", ticker: "DIS", price: 197.16),
    Stock(name: "Redfin", ticker: "RDFN", price: 145.06)
]
#endif
