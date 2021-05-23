//
//  StockCellTestViewModelTests.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 18.05.21.
//

import XCTest
import SwiftUI
import Resolver
@testable import Stock_Checker

class StockCellViewModelTests: XCTestCase {
    
    var sut: StockCellViewModel!
    var redStock = testDataStock[0]
    var greenStock = testDataStock[2]

    override func setUpWithError() throws {
        try super.setUpWithError()
        Resolver.register { TestDataStockRepository() as StockRepository }.scope(.application)
    }

    override func tearDownWithError() throws {
        sut = nil
        try super.tearDownWithError()
    }

    func testRedBackground() {
        //when
        sut = StockCellViewModel(stock: redStock)
        
        //then
        XCTAssertEqual(sut.backgroundColor, Color.red, "Conputed color is red")
    }
    
    func testGreenBackground() {
        //when
        sut = StockCellViewModel(stock: greenStock)
        
        //then
        XCTAssertEqual(sut.backgroundColor, Color.green, "Conputed color is green")
    }
}
