document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    chatForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const userMessage = userInput.value;
        appendMessage("user", userMessage);
        userInput.value = "";

        try {
            // Step 1: Send initial message to start task
            const startResponse = await fetch("/get", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ msg: userMessage })
            });

            if (!startResponse.ok) {
                throw new Error("Failed to start task.");
            }

            const { task_id } = await startResponse.json();

            // Step 2: Poll for result
            let result;
            while (!result) {
                const pollResponse = await fetch(`/result/${task_id}`);
                const pollData = await pollResponse.json();

                if (pollData.status === "processing") {
                    await new Promise((resolve) => setTimeout(resolve, 2000)); // Wait 2 seconds before next poll
                } else if (pollData.Response) {
                    result = pollData.Response;
                } else {
                    throw new Error("Failed to retrieve result.");
                }
            }

            // Display the response from the bot
            appendMessage("bot", result);

        } catch (error) {
            console.error("Error:", error);
            appendMessage("bot", "Sorry, there was an issue retrieving the response.");
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