function addMessage(text, type) {
    let chatBox = document.getElementById("chat-box");

    let msg = document.createElement("div");
    msg.className = "message " + type;
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    let input = document.getElementById("message");
    let text = input.value;

    if (text === "") return;

    addMessage(text, "user");

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.reply || "No reply", "bot");
    })
    .catch(err => {
        addMessage("Error ❌", "bot");
        console.log(err);
    });

    input.value = "";
}
function loadHistory() {
    fetch("/history")
    .then(res => res.json())
    .then(data => {
        let box = document.getElementById("history-box");

        data.history.forEach(item => {
            let div = document.createElement("div");
            div.innerText = item[0]; // message
            div.classList.add("history-item");

            box.appendChild(div);
        });
    });
}

window.onload = function() {
    loadHistory();
};