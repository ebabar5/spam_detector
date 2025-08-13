document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("analyze-btn");
  btn.addEventListener("click", function () {
    const mi = document.getElementById("message-input").value;
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: mi })
    })
      .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      })
      .then(data => {
        const labelRaw = data && data.label;
        const confidence = typeof data.confidence === "number" ? data.confidence : null;
        const isSpam = String(labelRaw).toLowerCase() === "spam" || Number(labelRaw) === 1;

        const resultSection = document.getElementById("result-section");
        const resultBadge = document.getElementById("result-badge");
        const resultText = document.getElementById("result-text");
        const progressBar = document.getElementById("progress-bar");
        const progressText = document.getElementById("progress-text");

        if (resultSection && resultBadge && resultText) {
	      resultSection.style.display = "block";
	      resultSection.classList.add("show");
	      resultBadge.textContent = isSpam ? "SPAM" : "HAM";
	      resultBadge.className = "result-badge " + (isSpam ? "spam" : "legitimate");
          
          resultText.textContent = isSpam ? "This looks like spam." : "This looks legitimate (ham).";

          
          if (progressBar && progressText && confidence !== null) {
            const pct = Math.round(confidence * 100);
            progressBar.style.width = `${pct}%`;
            progressText.textContent = `${pct}%`;
            progressBar.classList.remove("high-confidence", "medium-confidence", "low-confidence");
            if (pct >= 70) progressBar.classList.add("high-confidence");
            else if (pct >= 40) progressBar.classList.add("medium-confidence");
            else progressBar.classList.add("low-confidence");
          }
        } else {
          console.log("Result:", isSpam ? "spam" : "ham");
        }
      })
      .catch(console.error);
  });
});