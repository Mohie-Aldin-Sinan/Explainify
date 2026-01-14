import streamlit as st
from langchain_core.prompts import load_prompt
from llm_loader import load_llm
from pathlib import  Path

st.set_page_config(page_title="Explainify", page_icon="🧠")

st.title("Explainify 🧠✨")
st.write("View complex topics through a clear learning lens.")

BASE_DIR = Path(__file__).resolve().parent

llm = load_llm()

template_path = BASE_DIR / "prompt_template.json"
template = load_prompt(str(template_path))

concept_input = st.text_input("Enter a concept to explain")

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short", "Medium", "Long"]
)

if st.button("Explain"):
    if concept_input.strip() == "":
        st.warning("Please enter a concept first.")
    else:
        chain = template | llm
        result = chain.invoke({
            "concept_input": concept_input,
            "style_input": style_input,
            "length_input": length_input
    })
    st.write(result.content)

