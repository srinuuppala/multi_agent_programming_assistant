import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq

load_dotenv()

# 🔒 HARD LOCK THE MODEL (THIS IS THE KEY)
llm = Groq(
    id="llama-3.1-8b-instant",      # 👈 FORCE model ID
    model="llama-3.1-8b-instant",   # secondary safety
    tools=None,                # disable tool routing
    temperature=0.1
)

print("✅ FINAL GROQ MODEL:", llm.id)

# Developer Agent
developer_agent = Agent(
    name="Developer Agent",
    role="Software Developer",
    model=llm,
    instructions=[
        "Write clean, optimized Python code",
        "Follow best practices",
        "Add comments"
    ],
)

# QA Agent
qa_agent = Agent(
    name="QA Agent",
    role="QA Engineer",
    model=llm,
    instructions=[
        "Find bugs and fix them",
        "Return corrected Python code only"
    ],
)

# Reviewer Agent
reviewer_agent = Agent(
    name="Reviewer Agent",
    role="Senior Code Reviewer",
    model=llm,
    instructions=[
        "Validate logic correctness",
        "Check edge cases",
        "Reply with APPROVED or NEEDS FIX"
    ],
)

# PDF / Documentation Agent
pdf_agent = Agent(
    name="PDF Agent",
    role="Documentation Generator",
    model=llm,
    instructions=[
        "Format the provided content into a clear, structured document",
        "Use headings and sections",
        "Do NOT add extra explanation"
    ],
)

