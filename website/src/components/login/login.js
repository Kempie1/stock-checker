import React from "react";
import "./login.css"
import { useAuth } from "../../providers/AuthProvider";


export default function Login() {
  const {signInWithGoogle,signInWithApple} = useAuth()
  return (
    <div className="login-container">
      <div className="login-buttons">
        <button className="login-provider-button" onClick={signInWithGoogle}>
        <img src="https://img.icons8.com/ios-filled/50/000000/google-logo.png" alt="google icon"/>
        <span> Continue with Google</span>
       </button>
      </div>
    </div>
  );
}