//
//  StocksListViewModelTests.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 18.05.21.
//

import XCTest
import Resolver
@testable import Stock_Checker

class StocksListViewModelTests: XCTestCase {
    
    var sut: StocksListViewModel!
    var repository: StockRepository!

    override func setUpWithError() throws {
        try super.setUpWithError()
        sut = StocksListViewModel()
        repository = Resolver.resolve()
    }

    override func tearDownWithError() throws {
        sut = nil
        try super.tearDownWithError()
    }
    
    func test() throws {
        // given
        
    }

}
