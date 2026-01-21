# 🧠 Multi-Agent Programming Assistant using Agentic AI

A **Multi-Agent Programming Assistant** that simulates a real-world software development workflow using **Agentic AI architecture**.  
The system decomposes the software development lifecycle into multiple autonomous agents that collaboratively generate, debug, validate, and refine code.

---

## 🚀 Project Overview

This project demonstrates how **Agentic AI** can improve code quality, correctness, and reliability by separating responsibilities across multiple AI agents, similar to roles in a real software engineering team.

### Agents involved:
- 👨‍💻 **Developer Agent** – Writes initial code
- 🧪 **QA Agent** – Debugging and error fixing
- 🧑‍🏫 **Reviewer Agent** – Logic validation and approval

The agents collaborate iteratively until the final solution meets validation criteria.

---

## 🧩 System Architecture

User Input
↓
Developer Agent (Code Generation)
↓
QA Agent (Bug Fixing)
↓
Reviewer Agent (Validation)
↓
Iterative Refinement Loop
↓
Final Approved Output


---

## ⚙️ Tech Stack

- Python 3.13
- PhiData – Agent orchestration framework
- Groq (LLaMA 3) – Large Language Model
- Streamlit – User Interface
- python-dotenv – Environment variable management

---

## 📂 Project Structure

multi_agent_programming_assistant/
│
├── app.py # Streamlit UI
├── agents.py # Agent definitions (Developer, QA, Reviewer)
├── pipeline.py # Agent orchestration logic
├── requirements.txt
├── .env # Groq API key
└── README.md


---

## 🔁 Workflow Explanation

1. User enters a programming query.
2. Developer Agent generates initial Python code.
3. QA Agent analyzes and fixes errors.
4. Reviewer Agent validates logic and edge cases.
5. If not approved, feedback is sent back and the loop continues.
6. The process stops once the code is **APPROVED**.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt


2️⃣ Set Groq API key

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

3️⃣ Run the Streamlit app
streamlit run app.py

🧪 Sample Input
Write a Python function to check whether a number is prime.

✅ Output

Clean Python code

Debugged and optimized

Logic validated by Reviewer Agent

Approved after iterative refinement
