const API_BASE = "http://127.0.0.1:8000";

export async function sendMessage(message: string) {
  try {
    const response = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: message }),
    });

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const data = await response.json();
    // ✅ return the whole object so frontend can access res.response
    return { response: data.response };
  } catch (error) {
    return { response: "Error connecting to backend." };
  }
}
