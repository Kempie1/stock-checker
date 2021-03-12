//
//  AccountView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 12.03.21.
//

import SwiftUI

struct AccountView: View {
    @State var showSettingsScreen = false
    
    var body: some View {
        VStack{
            Text("Looks like you're not signed in yet")
            
            Button(action: {
                self.showSettingsScreen.toggle()
            }) {
                ZStack {
                    Capsule()
                        .fill(Color.blue)
                        .frame(width: 100, height: 50)
                    Text("Sign In")
                        .foregroundColor(.white)
                }
            }
            .sheet(isPresented: $showSettingsScreen) {
                SignInView()
            }
        }
    }
}

struct AccountView_Previews: PreviewProvider {
    static var previews: some View {
        AccountView()
    }
}
