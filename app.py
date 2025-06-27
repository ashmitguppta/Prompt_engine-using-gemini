import streamlit as st
from prompt_engine import run_prompt

#Creating a Streamlit page
st.set_page_config(page_title="Prompt Enngineerign App",layout= 'centered')

st.title("Prompt Engineering App")
#prompt types dropdown
prompt_types = [
    "Zero-Shot",
    "Few Shot",
    "Instruction-Based",
    "Chain-of-Thought",
    "Role-Based"
]

selected_prompt = st.selectbox("Choose prompt Type :",prompt_types)
user_input = st.text_area("Enter your prompt over here : ",height = 150)

if st.button("Generate the content "):
    with st.spinner("Generating Content..."):
        output = run_prompt(selected_prompt,user_input)
        st.markdown("Response: ")
        st.code(output)
