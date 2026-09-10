from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama


app = FastAPI(
    title="AI Student Support Assistant",
    version="1.0"
)


# Allow HTML/JavaScript frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Student(BaseModel):

    name: str = "Student"
    course: str = "B.E CSE - AI & ML"
    year: str = "Final Year"
    goal: str = "Software Engineer"


class ChatRequest(BaseModel):

    question: str
    student: Student


def detect_intent(question):

    text = question.lower()

    if any(word in text for word in [
        "dsa",
        "data structure",
        "algorithm",
        "leetcode",
        "coding"
    ]):
        return "DSA"

    if any(word in text for word in [
        "placement",
        "interview",
        "job",
        "company",
        "zoho",
        "mnc"
    ]):
        return "PLACEMENT"

    if any(word in text for word in [
        "project",
        "final year project",
        "mini project"
    ]):
        return "PROJECT"

    if any(word in text for word in [
        "aptitude",
        "reasoning",
        "percentage",
        "profit",
        "ratio"
    ]):
        return "APTITUDE"

    if any(word in text for word in [
        "study",
        "subject",
        "exam",
        "academic"
    ]):
        return "ACADEMIC"

    if any(word in text for word in [
        "career",
        "skill",
        "resume",
        "salary"
    ]):
        return "CAREER"

    return "GENERAL"


def get_context(intent):

    contexts = {

        "DSA": """
You are helping a student learn DSA.

Important topics:
- Arrays
- Strings
- Hashing
- Linked Lists
- Stack
- Queue
- Trees
- Graphs
- Searching
- Sorting
- Dynamic Programming

Give beginner-friendly explanations and examples.
""",

        "PLACEMENT": """
You are a placement preparation assistant.

Help students prepare:
- Programming
- DSA
- SQL
- Aptitude
- OOP
- DBMS
- OS
- Computer Networks
- HR interview
- Technical interview
""",

        "PROJECT": """
You are a final-year project mentor.

Suggest practical projects using:
- Python
- AI/ML
- Agentic AI
- Ollama
- HTML
- CSS
- JavaScript
- SQL

Projects should be realistic for students.
""",

        "APTITUDE": """
You are an aptitude trainer.

Teach:
- Percentages
- Profit and Loss
- Ratio
- Average
- Time and Work
- Time Speed Distance
- Probability
- Permutation
- Combination
- Number Systems
- Logical Reasoning

Give formulas and simple examples.
""",

        "ACADEMIC": """
You are an academic study assistant.

Help students with:
- Study planning
- Exam preparation
- Subject revision
- Time management
- Learning strategies
""",

        "CAREER": """
You are a career advisor for engineering students.

Give practical advice about:
- Software Engineering
- Data Analytics
- AI/ML
- Resume preparation
- Interview preparation
- Skills
- Projects
""",

        "GENERAL": """
You are a helpful student support assistant.
Answer student questions clearly and accurately.
"""
    }

    return contexts.get(intent, contexts["GENERAL"])


def ask_ollama(question, student, intent):

    system_prompt = f"""
You are an AI Student Support Assistant.

Student information:
Name: {student.name}
Course: {student.course}
Year: {student.year}
Career Goal: {student.goal}

Current intent: {intent}

{get_context(intent)}

Rules:
1. Use simple beginner-friendly language.
2. Give practical steps.
3. Use bullet points when useful.
4. Do not invent personal information.
5. For coding questions, provide correct code.
6. For study plans, give realistic schedules.
7. Keep answers relevant to the student's question.
"""


    response = ollama.chat(

        model="gemma3:4b",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],

        options={
            "temperature": 0.3
        }
    )

    return response["message"]["content"]


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "AI Student Support Assistant API"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    intent = detect_intent(request.question)

    try:

        answer = ask_ollama(
            request.question,
            request.student,
            intent
        )

        return {
            "answer": answer,
            "intent": intent
        }

    except Exception as error:

        return {
            "answer": (
                "Ollama connection failed.\n\n"
                "Make sure Ollama is installed, running, "
                "and the gemma3:4b model is available."
            ),
            "intent": intent,
            "error": str(error)
        }
