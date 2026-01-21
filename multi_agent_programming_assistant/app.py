import streamlit as st
import os

from pipeline import multi_agent_pipeline
from pdf_generator import generate_pdf

# --------------------------------------------------
# Page Configuration (MUST be first Streamlit call)
# --------------------------------------------------
st.set_page_config(
    page_title="Multi-Agent Programming Assistant",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🧠 Multi-Agent Programming Assistant")
st.caption("Agentic AI using PhiData + Groq")

# --------------------------------------------------
# User Input
# --------------------------------------------------
user_query = st.text_area(
    "Enter your programming problem:",
    placeholder="Example: Write a Python function to check whether a number is prime",
    height=150,
    key="user_query_input"
)

generate_btn = st.button("🚀 Generate Code", key="generate_code_btn")

# --------------------------------------------------
# Run Agents
# --------------------------------------------------
if generate_btn:
    if not user_query.strip():
        st.warning("Please enter a programming problem.")
    else:
        with st.spinner("Agents are working..."):
            result = multi_agent_pipeline(user_query)

        # Store result in session state
        st.session_state["result"] = result

        st.success(f"Approved in {result['iterations']} iteration(s)")

# --------------------------------------------------
# Display Output + PDF Generation
# --------------------------------------------------
if "result" in st.session_state:
    result = st.session_state["result"]

    st.divider()

    st.subheader("✅ Final Code")
    st.code(result["final_code"], language="python")

    st.subheader("🧐 Reviewer Feedback")
    st.write(result["review_feedback"])

    st.divider()

    # --------------------------------------------------
    # Generate PDF
    # --------------------------------------------------
    if st.button("📄 Generate PDF", key="generate_pdf_btn"):
        pdf_path = generate_pdf(
            result["full_text"],
            file_path="multi_agent_output.pdf"
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="⬇️ Download PDF",
                data=pdf_file,
                file_name="multi_agent_programming_output.pdf",
                mime="application/pdf"
            )