import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    fetch("/api/health")
      .then((res) => res.json())
      .then((data) => setStatus(`backend: ${data.status}, db: ${data.db}`))
      .catch(() => setStatus("backend unreachable — is uvicorn running on :8000?"));
  }, []);

  return (
    <div style={{ fontFamily: "sans-serif", padding: "2rem" }}>
      <h1>Scaffold</h1>
      <p>{status}</p>
    </div>
  );
}

export default App;
