document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    chatForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const userMessage = userInput.value;
        appendMessage("user", userMessage);
        userInput.value = "";

        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 300000); // 5-minute timeout

        try {
            const response = await fetch("/get", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({ msg: userMessage }),
                signal: controller.signal // Use AbortController's signal
            });

            clearTimeout(timeoutId); // Clear timeout if response received

            if (response.ok) {
                const data = await response.json();
                appendMessage("bot", data.Response);
            } else {
                console.error("Server error:", response.statusText);
                appendMessage("bot", "Sorry, there was an issue retrieving the response.");
            }
        } catch (error) {
            if (error.name === 'AbortError') {
                console.error("Fetch timeout:", error);
                appendMessage("bot", "The server is taking too long to respond. Please try again later.");
            } else {
                console.error("Network error:", error);
                appendMessage("bot", "Sorry, a network error occurred.");
            }
        }
    });

    function appendMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender === "user" ? "user-message" : "bot-message");

        const messageContent = document.createElement("div");
        messageContent.classList.add("message-content");
        messageContent.innerHTML = message;

        messageDiv.appendChild(messageContent);
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});