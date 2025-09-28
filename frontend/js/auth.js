const API_BASE = "http://localhost:8000/auth";

async function signup() {
  const username = document.getElementById("signup-username").value;
  const password = document.getElementById("signup-password").value;

  const res = await fetch(`${API_BASE}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  document.getElementById("signup-result").innerText = data.msg || data.detail;
}

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();

  if (data.access_token && data.user_id) {
    localStorage.setItem("token", data.access_token);  // ✅ Save token
    localStorage.setItem("user_id", data.user_id);     // ✅ Save user ID
    window.location.href = "landing.html";               // ✅ Redirect
  } else {
    alert("Login failed.");
  }
}

