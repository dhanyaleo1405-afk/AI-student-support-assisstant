const API_URL = "http://127.0.0.1:8000/chat";

function getStudentProfile() {

    return {
        name: document.getElementById("studentName").value || "Student",
        course: document.getElementById("course").value || "B.E CSE - AI & ML",
        year: document.getElementById("year").value,
        goal: document.getElementById("goal").value || "Software Engineer"
    };
}


function addMessage(sender, message) {

    const chatBox = document.getElementById("chatBox");

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (sender === "user") {
        messageDiv.classList.add("user");
    } else {
        messageDiv.classList.add("bot");
    }

    const content = document.createElement("div");

    content.classList.add("message-content");

    const title = document.createElement("strong");

    title.textContent = sender === "user"
        ? "You"
        : "AI Assistant";

    const paragraph = document.createElement("p");

    paragraph.textContent = message;

    content.appendChild(title);
    content.appendChild(paragraph);

    messageDiv.appendChild(content);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const input = document.getElementById("userInput");

    const question = input.value.trim();

    if (question === "") {
        return;
    }

    addMessage("user", question);

    input.value = "";

    document.getElementById("typing").style.display = "block";

    const student = getStudentProfile();

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question,
                student: student
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Server error");
        }

        addMessage("bot", data.answer);

    } catch (error) {

        addMessage(
            "bot",
            "❌ Unable to connect to the AI server.\n\n" +
            "Please make sure Ollama and the Python server are running."
        );

        console.error(error);

    } finally {

        document.getElementById("typing").style.display = "none";
    }
}


function quickQuestion(question) {

    document.getElementById("userInput").value = question;

    sendMessage();
}


function handleKeyPress(event) {

    if (event.key === "Enter") {
        sendMessage();
    }
}
