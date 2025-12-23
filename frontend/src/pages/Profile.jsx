import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Profile() {
  const [profile, setProfile] = useState(null);
  const [showAadhaar, setShowAadhaar] = useState(false);

  useEffect(() => {
    api.get("profile/").then((res) => setProfile(res.data));
  }, []);

  const logout = () => {
    localStorage.removeItem("access");
    window.location.reload();
  };

  if (!profile) return <p>Loading...</p>;

  const maskedAadhaar =
    "XXXXXXXX" + profile.aadhaar.slice(-4);

  return (
    <div className="card">
      <h2>User Profile</h2>

      <p><b>Username:</b> {profile.username}</p>
      <p><b>Email:</b> {profile.email}</p>

      <p style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <b>Aadhaar:</b>
        <span>
          {showAadhaar ? profile.aadhaar : maskedAadhaar}
        </span>
        <button
          onClick={() => setShowAadhaar(!showAadhaar)}
          style={{
            background: "transparent",
            border: "none",
            cursor: "pointer",
            fontSize: "16px"
          }}
          title={showAadhaar ? "Hide Aadhaar" : "Show Aadhaar"}
        >
          {showAadhaar ? "🙈" : "👁️"}
        </button>
      </p>

      <button style={{ marginTop: "15px" }} onClick={logout}>
        Logout
      </button>
    </div>
  );
}
