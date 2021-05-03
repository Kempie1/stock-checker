import React, {  useState  } from 'react';
import {  useAuth  } from "../../providers/AuthProvider"
import { BrowserRouter as Router, useHistory } from "react-router-dom"

const Home = (props) => {
const [error, setError] = useState("")
const { currentUser, logout } = useAuth()
console.log(currentUser)



const history = useHistory()

  async function handleLogout() {
    setError("")

    try {
      await logout()
      history.push("/login")
    } catch {
      setError("Failed to log out")
    }
  }
  




  return (
    <div>
    {error && <div>{error}</div>}
    Home {currentUser.displayName}
  <div className="w-100 text-center mt-2">
        <button variant="link" onClick={handleLogout}>
          Log Out
        </button>
      </div>
    </div>
    
  );
};

export default Home;