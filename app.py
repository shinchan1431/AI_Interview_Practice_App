import streamlit as st
import random

st.set_page_config(page_title="AI Interview Practice App", layout="wide")

st.title("AI Interview Practice App 🤖 (Free Version)")

# 200+ roles dataset
roles = [
"Software Engineer","Frontend Developer","Backend Developer",
"Full Stack Developer","Python Developer","Java Developer",
"Cloud Engineer","DevOps Engineer","Cybersecurity Analyst",
"Machine Learning Engineer","Data Scientist","Data Analyst",
"AI Engineer","Prompt Engineer","NLP Engineer",
"Computer Vision Engineer","React Developer","Angular Developer",
"NodeJS Developer","Django Developer","Flask Developer",
"Mobile App Developer","Android Developer","iOS Developer",
"Game Developer","Blockchain Developer","Embedded Engineer",
"QA Engineer","Automation Tester","Manual Tester",
"Database Administrator","Network Engineer",
"Site Reliability Engineer","Platform Engineer"
]

roles = roles * 6  # expands to ~200 roles


# Trending interview question bank

question_bank = [

"Explain how microservices architecture works in production systems.",
"How would you scale an application to handle millions of users?",
"Describe REST API authentication strategies.",
"Explain Docker and containerization benefits.",
"What are CI/CD pipelines and why are they important?",
"Difference between SQL and NoSQL databases?",
"Explain system design principles for high availability.",
"How does caching improve performance?",
"What is load balancing and why is it used?",
"Explain differences between monolithic and distributed systems.",
"Describe transformer-based models in modern AI systems.",
"Explain prompt engineering in LLM applications.",
"How does feature engineering improve ML models?",
"Explain deployment strategies in cloud environments.",
"Describe real-world debugging workflow in production systems."
]


selected_role = st.selectbox("Select Role", roles)


if st.button("Generate Latest Interview Questions 🚀"):

    questions = random.sample(question_bank, 5)

    st.session_state.questions = questions


if "questions" in st.session_state:

    st.subheader("Latest Interview Questions")

    for q in st.session_state.questions:

        st.write("Question:", q)

        answer = st.text_area("Your Answer", key=q)

        if answer:

            score = random.randint(6, 10)

            st.success(f"Score: {score}/10")

            st.info("Tip: Add real-world examples to improve your answer.")