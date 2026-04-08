import streamlit as st
import matplotlib.pyplot as plt

st.title("Mood Assessment Graphs")

if "depression_score" in st.session_state:

    d = st.session_state.depression_score
    m = st.session_state.mania_score

    st.subheader("Depression vs Mania Score")

    labels = ['Depression Score', 'Mania Score']
    values = [d, m]

    fig = plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Score Type")
    plt.ylabel("Score Value")
    plt.title("Mood Disorder Assessment Scores")

    st.pyplot(fig)

else:
    st.warning("Please complete the patient assessment first.")

