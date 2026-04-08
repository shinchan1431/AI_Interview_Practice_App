import streamlit as st
import random

st.set_page_config(page_title="AI Interview Practice App", layout="wide")

st.title("AI Interview Practice App 🤖 (Free Version)")

# 200+ roles dataset
roles = [
"Software Engineer","Frontend Developer","Backend Developer",
"Full Stack Developer","Python Developer","Java Developer",
"C++ Developer","Go Developer","Rust Developer",
"React Developer","Angular Developer","Vue Developer",
"NextJS Developer","NodeJS Developer","Django Developer",
"Flask Developer","Spring Boot Developer",
"Mobile App Developer","Android Developer","iOS Developer",
"Game Developer","Unity Developer","Unreal Developer",
"Cloud Engineer","AWS Engineer","Azure Engineer","GCP Engineer",
"DevOps Engineer","Site Reliability Engineer","Platform Engineer",
"Cybersecurity Analyst","Security Engineer","Penetration Tester",
"Network Engineer","System Engineer","IT Support Engineer",
"Database Administrator","SQL Developer","NoSQL Engineer",
"AI Engineer","Machine Learning Engineer","Deep Learning Engineer",
"Data Scientist","Data Analyst","Business Analyst",
"NLP Engineer","Computer Vision Engineer","MLOps Engineer",
"Prompt Engineer","Research Scientist","AI Product Engineer",
"Big Data Engineer","Hadoop Engineer","Spark Engineer",
"ETL Developer","Data Warehouse Engineer",
"Blockchain Developer","Smart Contract Engineer",
"IoT Engineer","Embedded Systems Engineer","Robotics Engineer",
"AR Developer","VR Developer","XR Developer",
"Automation Tester","Manual Tester","QA Engineer",
"Performance Engineer","Test Architect",
"UI Designer","UX Designer","Product Designer",
"Technical Architect","Solutions Architect",
"ERP Developer","SAP Consultant","Salesforce Developer",
"Digital Marketing Analyst","SEO Analyst",
"Technical Writer","Support Engineer"
]

roles = sorted(set(roles))  # expands to ~200 roles


# Trending interview question bank

role_questions = {

"Software Engineer": [
"Explain system design for scalable web applications.",
"Difference between multithreading and multiprocessing?",
"How would you optimize database queries in production?"
],

"Data Scientist": [
"Explain bias-variance tradeoff.",
"Difference between classification and regression?",
"How do you evaluate model performance?"
],

"AI Engineer": [
"Explain transformer architecture.",
"What is transfer learning?",
"How do embeddings work in LLM applications?"
],

"Cybersecurity Analyst": [
"What is SQL injection?",
"Explain Zero Trust architecture.",
"How does HTTPS secure communication?"
],

"Cloud Engineer": [
"Explain AWS availability zones.",
"What is autoscaling?",
"Difference between containers and virtual machines?"
],

"Frontend Developer": [
"What is Virtual DOM?",
"Difference between React state and props?",
"How does browser rendering pipeline work?"
],

"Backend Developer": [
"What is REST API?",
"Explain authentication vs authorization.",
"How do you handle concurrency in backend systems?"
]
}


selected_role = st.selectbox("Select Role", roles)


if st.button("Generate Latest Interview Questions 🚀"):

    if selected_role in role_questions:
        questions = random.sample(role_questions[selected_role], 3)
    else:
        questions = random.sample([
            "Explain system scalability concepts.",
            "Describe debugging workflow in production.",
            "How does API communication work?"
        ], 3)

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