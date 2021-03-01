//
//  StockTextView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 01.03.21.
//

import SwiftUI

struct StockTextView: View {
    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                Text("Stock Name")
                    .font(.largeTitle)
                Spacer()
                Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/, label: {
                    ZStack {
                        Capsule()
                            .fill(Color.blue)
                            .frame(width: 100, height: 50)
                        Text("Button")
                            .foregroundColor(.white)
                    }
                })
            }
            Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent a turpis vehicula, condimentum nulla in, mollis arcu. Vivamus felis diam, condimentum nec finibus vel, lacinia ut odio. Curabitur varius mattis arcu, sed euismod purus fringilla ut. Quisque id fermentum nisl, vel laoreet lectus. Curabitur egestas imperdiet dictum. Morbi lobortis commodo blandit.")
        }
    }
}

struct StockTextView_Previews: PreviewProvider {
    static var previews: some View {
        StockTextView()
    }
}
