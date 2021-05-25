//
//  ExploreViewSnapshotTests.swift
//  Stock CheckerTests
//
//  Created by Valentin Silvera on 24.05.21.
//

import XCTest
import SwiftUI
import SnapshotTesting

@testable import Stock_Checker

class ExploreViewSnapshotTests: XCTestCase {

    func testDefaultAppereance() {
        let vc = ExploreView().toVC()
        
        assertSnapshot(matching: vc, as: .image)
    }

    func testDynamicFonts() {
        let view = ExploreView()
        
        assertSnapshot(matching: view.environment(\.sizeCategory, ContentSizeCategory.extraSmall).toVC(), as: .image, named: "xs")
        
        assertSnapshot(matching: view.environment(\.sizeCategory, ContentSizeCategory.extraExtraExtraLarge).toVC(), as: .image, named: "xxxl")
        
        assertSnapshot(matching: view.environment(\.sizeCategory, ContentSizeCategory.accessibilityExtraExtraExtraLarge).toVC(), as: .image, named: "accessibility xxxl")
    }
    
    func testColorSchemes() {
        let view = ExploreView()
        
        assertSnapshot(matching: view.colorScheme(.light).toVC(), as: .image)
        assertSnapshot(matching: view.colorScheme(.dark).toVC(), as: .image)
    }
}

extension SwiftUI.View {
    func toVC() -> UIViewController {
        let vc = UIHostingController(rootView: self)
        vc.view.frame = UIScreen.main.bounds
        return vc
    }
}
