//
//  Test.swift
//  Stock Checker
//
//  Created by Maximilian Hues on 17.04.21.
//

import SwiftUI

struct ProfileList: View {
 
    var body: some View {
        ZStack {
            Color.white
            VStack(alignment: .center, spacing: 30) {
                Text("Congratulations").foregroundColor(Color.black)
                    .padding(.horizontal, 100)
                    .font(.system(size: 15, weight: .heavy, design: .default))
                VStack(alignment: .leading, spacing: 10) {
                    Text("Score:").foregroundColor(Color.black)
                    Text("Level:").foregroundColor(Color.black)
                    Text("You can go back now!").foregroundColor(Color.black)
                    Text("Start with the next level!").foregroundColor(Color.black)
                }
                Button(action: {
                    
                }, label: {
                    Text("Close")
                })
            }.padding()
        }
        .frame(width: 360, height: 250)
        .cornerRadius(20).shadow(radius: 20)
    }
    }


struct ProfileList_Previews: PreviewProvider {
    static var previews: some View {
        ProfileList()
    }
}
