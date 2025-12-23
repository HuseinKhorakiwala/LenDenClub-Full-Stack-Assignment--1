import { useState } from "react";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import "./index.css";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(
    !!localStorage.getItem("access")
  );

  return (
    <div className="container">
      {loggedIn ? (
        <Profile />
      ) : (
        <Login onLogin={() => setLoggedIn(true)} />
      )}
    </div>
  );
}
