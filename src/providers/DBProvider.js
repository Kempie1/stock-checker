import React from "react";
import { database } from "../services/firebase"
import Firebase from "firebase";
import config from "./config";

export function writeUserData() {
    Firebase.database()
      .ref("/")
      .set(this.state);
    console.log("DATA SAVED");
  };

  export  function getUserData(){
    let ref = Firebase.database().ref("/");
    ref.on("value", snapshot => {
      const state = snapshot.val();
      this.setState(state);
    });
  };