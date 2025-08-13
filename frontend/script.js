document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("analyze-btn");
    btn.addEventListener("click", function (e) {
      e.preventDefault();
const mi=document.getElementById("message-input").value;
fetch('http://localhost:5000/predict',{
    method:'POST',
    headers:{'content-Type':'application/json'},
    body:JSON.stringify({message:mi})
}).then(response=>response.json())
  .then(data => {
    const prediction = data[0]; 
    
    const isSpam = prediction === 1;
    
    document.getElementById("result-section").style.display = "block";
    
    const badge = document.getElementById("result-badge");
    badge.textContent = isSpam ? "SPAM" : "LEGITIMATE";
    badge.className = isSpam ? "result-badge spam" : "result-badge legitimate";
    
    const resultText = document.getElementById("result-text");
    resultText.textContent = isSpam ? 
        "This message appears to be spam. Be cautious!" : 
        "This message appears to be legitimate.";
    const confidence = 85;
    document.getElementById("progress-bar").style.width = confidence + "%";
    document.getElementById("progress-text").textContent = confidence + "%";
})
})
  });