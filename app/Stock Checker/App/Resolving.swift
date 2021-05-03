//
//  Resolving.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 22.04.21.
//

import Foundation
import Resolver

extension Resolver: ResolverRegistering {
    public static func registerAllServices() {
        register { TestDataStockRepository() as StockRepository }.scope(.application)
    }
}
