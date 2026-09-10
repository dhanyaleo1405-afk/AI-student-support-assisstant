# 🎓 AI Student Support Assistant

An **AI-powered Student Support Assistant** developed using **Agentic AI concepts, HTML, CSS, JavaScript, FastAPI, and Ollama**.

The system helps students with **DSA, placement preparation, aptitude, academics, projects, career guidance, and interview preparation** through a simple web interface.

---

## 📌 Project Title

**AI Student Support Assistant using Agentic AI and Ollama**

---

## 🎯 Objective

The main objective of this project is to develop an intelligent student-support system that can:

* Answer student questions
* Provide DSA guidance
* Generate placement study plans
* Suggest final-year projects
* Help with aptitude preparation
* Provide career guidance
* Support academic preparation
* Give interview preparation advice

The application uses **Ollama** to run a local Large Language Model (LLM).

---

## ✨ Features

### 🤖 AI Chat Assistant

Students can ask questions using a simple chat interface.

### 💻 DSA Support

The assistant can help students learn:

* Arrays
* Strings
* Linked Lists
* Stack
* Queue
* Trees
* Graphs
* Searching
* Sorting
* Dynamic Programming

### 🎯 Placement Preparation

Provides guidance for:

* Coding
* DSA
* SQL
* Aptitude
* OOP
* DBMS
* Operating Systems
* Computer Networks
* Technical interviews
* HR interviews

### 🧠 Aptitude Preparation

Supports topics such as:

* Percentages
* Profit and Loss
* Ratio
* Average
* Time and Work
* Time, Speed and Distance
* Probability
* Permutation and Combination
* Number System
* Logical Reasoning

### 🚀 Project Suggestions

The assistant can suggest practical projects related to:

* AI
* Machine Learning
* Agentic AI
* Data Analytics
* Web Development
* Student Management

### 👩‍💻 Career Guidance

Students can receive guidance for:

* Software Engineer
* AI/ML Engineer
* Data Analyst
* Resume preparation
* Interview preparation
* Skill development

### 👤 Student Profile

The application allows students to enter:

* Name
* Course
* Year
* Career Goal

The information is sent to the AI assistant to make responses more relevant.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │     Student      │
                    └────────┬─────────┘
                             │
                             ▼
              ┌──────────────────────────┐
              │     HTML / CSS / JS      │
              │      Web Interface       │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │       FastAPI            │
              │       Backend            │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │    Intent Detection      │
              └────────────┬─────────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
            DSA        Placement      Project
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                 ┌─────────────────┐
                 │     Ollama      │
                 │   gemma3:4b     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  AI Response    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Web Browser   │
                 └─────────────────┘
```

---

# 🧩 Agentic AI Workflow

The system follows an agent-based workflow:

```text
Student Question
       ↓
Intent Detection
       ↓
Identify Student Requirement
       ↓
Select Appropriate Support Area
       ↓
Prepare Context
       ↓
Ollama LLM
       ↓
Generate Response
       ↓
Display Answer
```

### Example

If the student asks:

```text
Give me a 7 day DSA study plan
```

The system detects:

```text
Intent = DSA
```

Then the request is sent to Ollama with the DSA-related context.

The AI generates a personalized response.

---

# 🛠️ Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| HTML5      | Web page structure    |
| CSS3       | User interface design |
| JavaScript | Frontend interaction  |
| Python     | Backend programming   |
| FastAPI    | REST API              |
| Ollama     | Local AI/LLM          |
| Gemma 3    | Language model        |
| Uvicorn    | FastAPI server        |
| GitHub     | Version control       |

---

# 📂 Project Structure

```text
AI-Student-Support-Assistant/
│
├── index.html
│
├── style.css
│
├── script.js
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# ⚙️ Installation

## Step 1: Install Python

Make sure Python is installed.

Check:

```bash
python --version
```

---

## Step 2: Install Ollama

Install Ollama on your computer.

Check the installation:

```bash
ollama --version
```

---

## Step 3: Download the AI Model

Run:

```bash
ollama pull gemma3:4b
```

Test the model:

```bash
ollama run gemma3:4b
```

Type:

```text
Hello
```

If Ollama responds, the model is working correctly.

---

# 📦 Step 4: Create Virtual Environment

Open Command Prompt inside the project folder.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

# 📥 Step 5: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

# ▶️ Step 6: Start the Backend

Run:

```bash
uvicorn app:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

# 🌐 Step 7: Open the Frontend

Open:

```text
index.html
```

in Google Chrome or another browser.

The frontend communicates with the FastAPI backend.

---

# 🧪 Example Questions

Students can ask:

### DSA

```text
Explain Two Sum in simple terms
```

### Placement

```text
Create a 7 day placement study plan
```

### Aptitude

```text
Teach me percentage problems
```

### Project

```text
Suggest AI final year projects
```

### Career

```text
What skills are required for a software engineer?
```

### Interview

```text
Give me 10 technical interview questions
```

---

# 🖥️ Expected Output

The application provides a web interface containing:

```text
┌─────────────────────────────────────────────┐
│       🎓 AI Student Support Assistant       │
│          Powered by Agentic AI + Ollama      │
├───────────────┬─────────────────────────────┤
│ Student       │                              │
│ Profile       │     AI Assistant             │
│               │                              │
│ Name          │  Hello! How can I help you? │
│ Course        │                              │
│ Year          │  You: Give me a DSA plan    │
│ Career Goal   │                              │
│               │  AI: Here is your plan...   │
│ Quick Actions │                              │
│               │                              │
│ Placement     │                              │
│ DSA Questions │                              │
│ Project Ideas │                              │
│ Aptitude      │                              │
├───────────────┴─────────────────────────────┤
│ Ask your question...              [Send 🚀] │
└─────────────────────────────────────────────┘
```

---

# 🔐 Privacy

This project uses **Ollama locally**.

The AI model runs on the student's computer instead of requiring a cloud AI API key.

The project does not require storing an OpenAI API key or other paid AI API credentials.

---

# 🔮 Future Enhancements

The following features can be added in future versions:

* 📚 College FAQ chatbot
* 📄 PDF-based RAG
* 🧑‍🎓 Student login
* 💾 Chat history
* 📊 Student progress dashboard
* 📅 Automatic timetable generation
* 📝 AI quiz generation
* 📄 Resume analyzer
* 🎯 Skill-gap analysis
* 🏆 Placement readiness score
* 🧠 Multiple specialized AI agents
* 🗃️ SQLite/MySQL database
* 🎤 AI mock interview
* 📈 Student performance analytics

---

# 🎓 Internship Project

This project is developed as part of the:

**IBM TNSDC Agentic AI Internship Program – August 2026**

### Project Domain

**Artificial Intelligence / Agentic AI**

### Project Type

**AI-powered Web Application**

---

# 👩‍💻 Author

**Dhanyalakshmi B**

B.E. Computer Science and Engineering
Artificial Intelligence & Machine Learning

---

# 📜 License

This project is created for educational and internship purposes.
