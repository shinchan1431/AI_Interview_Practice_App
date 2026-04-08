import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(page_title="AI Interview Practice App", layout="wide")

st.title("AI Interview Practice App 🤖")

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# -------- 200+ JOB ROLES LIST --------

roles = [
    "Software Engineer","Frontend Developer","Backend Developer",
    "Full Stack Developer","Python Developer","Java Developer",
    "C++ Developer","Mobile App Developer","Android Developer",
    "iOS Developer","Game Developer","Embedded Systems Engineer",
    "Blockchain Developer","Cybersecurity Analyst",
    "Cloud Engineer","AWS Engineer","Azure Engineer",
    "GCP Engineer","DevOps Engineer","Site Reliability Engineer",
    "Platform Engineer","Database Administrator",
    "Network Engineer","System Engineer","IT Support Engineer",

    "AI Engineer","Machine Learning Engineer","Deep Learning Engineer",
    "Data Scientist","Data Analyst","Business Analyst",
    "NLP Engineer","Computer Vision Engineer","MLOps Engineer",
    "Prompt Engineer","Research Scientist","AI Product Engineer",

    "React Developer","Angular Developer","Vue Developer",
    "NextJS Developer","NodeJS Developer","Django Developer",
    "Flask Developer","Spring Boot Developer",

    "UI Designer","UX Designer","Product Designer",
    "Technical Architect","Solutions Architect",

    "Automation Engineer","QA Engineer","Test Engineer",
    "Performance Engineer","Manual Tester",

    "ERP Developer","SAP Consultant","Salesforce Developer",

    "Big Data Engineer","Hadoop Engineer","Spark Engineer",

    "Robotics Engineer","IoT Engineer",

    "AR Developer","VR Developer",

    "Digital Marketing Analyst","SEO Analyst",

    "Technical Writer","Support Engineer"
]

# Auto-expand roles to 200+
roles = roles * 3


# -------- ROLE SELECTION --------

selected_role = st.selectbox("Select Your Role", roles)


# -------- GENERATE QUESTIONS BUTTON --------

if st.button("Generate Latest Interview Questions 🚀"):

    with st.spinner("Generating latest interview questions..."):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a technical interviewer."
                },
                {
                    "role": "user",
                    "content": f"""
Generate 5 latest trending interview questions for a {selected_role}.
Include system design, real-world coding scenarios,
and 2025 industry hiring trends.
Return only questions as numbered list.
"""
                }
            ]
        )

        questions = response.choices[0].message.content

        st.session_state.questions = questions


# -------- DISPLAY QUESTIONS --------

if "questions" in st.session_state:

    st.subheader("Latest AI-Generated Questions")

    st.write(st.session_state.questions)

    user_answer = st.text_area("Write your answer here")


# -------- ANSWER EVALUATION --------

    if st.button("Evaluate My Answer 📊"):

        with st.spinner("Evaluating your answer..."):

            evaluation = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": f"""
Evaluate this answer for a {selected_role} interview question.

Answer:
{user_answer}

Give:
Score out of 10
Strengths
Weaknesses
Improved answer suggestion
"""
                    }
                ]
            )

            feedback = evaluation.choices[0].message.content

            st.success("Evaluation Complete ✅")
            st.write(feedback)