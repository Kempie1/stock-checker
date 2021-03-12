//
//  SignInView.swift
//  Stock Checker
//
//  Created by Valentin Silvera on 12.03.21.
//

import SwiftUI

struct SignInView: View {
    @Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>
    
    @State var signInHandler: SignInWithAppleCoordinator?
    
    var body: some View {
        VStack {
            SignInWithAppleButton()
                .frame(width: 280, height: 45)
                .onTapGesture {
                    self.signInHandler = SignInWithAppleCoordinator()
                    
                    if let coordinator = self.signInHandler {
                        coordinator.startSignInWithAppleFlow {
                            print("Successfully signed in")
                            self.presentationMode.wrappedValue.dismiss()
                        }
                    }
                }
        }
    }
}

struct SignInView_Previews: PreviewProvider {
    static var previews: some View {
        SignInView()
    }
}
