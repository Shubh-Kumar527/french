import streamlit as st
import random
from google import generativeai as genai

# Configure Gemini API key
GEMINI_API_KEY = 'AIzaSyCQGt3DkRf6BrkVV9HGWmtl9JrjdI6gEtA'
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# App title
st.title('🇫🇷 Welcome to the French Quiz 🇫🇷')

# Question list
question_list = [
    '1) What was the Bastille?',
    '2) When was the Bastille stormed?',
    '3) Why was the Bastille hated by all?',
    '4) Who led the storming of the Bastille?',
    '5) What is the historical significance of 14 July in France?',
    '6) How is Bastille Day celebrated in France?',
    '7) How is the fall of the Bastille remembered today?',
    '8) What is the most common activity in France during the Bastille Day celebration?'
]

# Only select a random question once
if 'question' not in st.session_state:
    st.session_state.question = random.choice(question_list)

# Show question
st.subheader("Question:")
st.write(st.session_state.question)

# User input
a = st.text_input('Enter your answer:')

# Check answer and display feedback
if a:
    prompt = f"Please check and evaluate this answer:\nQuestion: {st.session_state.question}\nAnswer: {a}\nIs it correct? Provide feedback."
    response = model.generate_content(prompt)
    st.write("### Feedback:")
    st.write(response.text)
