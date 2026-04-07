import streamlit as st

st.title("AI Interview Practice App 🤖")

roles = [
    "Software Engineer",
    "Data Scientist",
    "Web Developer",
    "Python Developer",
    "AI Engineer"
]

selected_role = st.selectbox("Select Role", roles)

questions = {
    "Software Engineer": [
        "Explain OOP concepts.",
        "What is time complexity?",
        "Difference between stack and queue?"
    ],

    "Data Scientist": [
        "Explain overfitting.",
        "Difference between supervised and unsupervised learning?",
        "What is feature engineering?"
    ],

    "Web Developer": [
        "Difference between HTML and CSS?",
        "What is JavaScript DOM?",
        "Explain REST API."
    ],

    "Python Developer": [
        "Explain Python lists vs tuples.",
        "What is lambda function?",
        "Explain decorators."
    ],

    "AI Engineer": [
        "What is neural network?",
        "Difference between ML and DL?",
        "Explain transformer models."
    ]
}

if selected_role:

    st.subheader("Interview Questions")

    for q in questions[selected_role]:

        st.write("Question:", q)

        user_answer = st.text_area("Your Answer", key=q)

        if user_answer:
            st.success("Good attempt! Keep practicing 🚀")