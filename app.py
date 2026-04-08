import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mood Disorder CDSS", layout="wide")

if "stage" not in st.session_state:
    st.session_state.stage = 0

def diagnose(d, m):
    if d >= 20:
        severity = "Severe Depression"
    elif d >= 15:
        severity = "Moderately Severe Depression"
    elif d >= 10:
        severity = "Moderate Depression"
    elif d >= 5:
        severity = "Mild Depression"
    else:
        severity = "Minimal Depression"

    if d >= 10 and m < 8:
        diagnosis = "Major Depressive Disorder"
    elif d >= 10 and m >= 8:
        diagnosis = "Bipolar Disorder"
    elif m >= 10:
        diagnosis = "Mania / Hypomania"
    elif d >= 5:
        diagnosis = "Dysthymia"
    else:
        diagnosis = "Cyclothymia"

    return diagnosis, severity


def treatment_plan(diagnosis):
    if diagnosis == "Major Depressive Disorder":
        return "CBT, Antidepressants, Lifestyle changes"
    elif diagnosis == "Bipolar Disorder":
        return "Mood stabilizers, Psychotherapy"
    elif diagnosis == "Mania / Hypomania":
        return "Mood stabilizers, Antipsychotics"
    elif diagnosis == "Dysthymia":
        return "Therapy, Antidepressants"
    else:
        return "Counseling and Monitoring"


if st.session_state.stage == 0:

    st.image("mood.png")
    st.title("Mood Disorder Clinical Decision Support System")

    st.markdown("""
    ### About This Application
    
    This application is designed to assist in the assessment of mood disorders 
    using standardized symptom-based evaluation.
    
    It helps to:
    - Collect patient information  
    - Perform mood assessment (PHQ-9 + Mania scale)  
    - Provide possible diagnosis  
    - Suggest treatment options  
    - Visualize assessment results  
    - Generate patient report  
    
    ---
    
    ### Disorders Included
    - Major Depressive Disorder  
    - Bipolar Disorder  
    - Mania / Hypomania  
    - Dysthymia  
    - Cyclothymia  
    """)

    if st.button("Start"):
        st.session_state.stage = 1


elif st.session_state.stage == 1:

    st.header("Patient Information")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Next"):
        if name == "":
            st.error("Enter patient name")
        else:
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.stage = 2


elif st.session_state.stage == 2:

    st.header("Assessment")

    st.subheader("Depression (PHQ-9)")

    q1 = st.slider("Interest loss", 0, 3)
    q2 = st.slider("Feeling depressed", 0, 3)
    q3 = st.slider("Sleep issues", 0, 3)
    q4 = st.slider("Low energy", 0, 3)
    q5 = st.slider("Appetite change", 0, 3)
    q6 = st.slider("Low self-worth", 0, 3)
    q7 = st.slider("Concentration issues", 0, 3)
    q8 = st.slider("Restlessness", 0, 3)
    q9 = st.slider("Self-harm thoughts", 0, 3)

    st.subheader("Mania Symptoms")

    m1 = st.slider("Elevated mood", 0, 3)
    m2 = st.slider("High energy", 0, 3)
    m3 = st.slider("Less sleep", 0, 3)
    m4 = st.slider("Racing thoughts", 0, 3)
    m5 = st.slider("Impulsiveness", 0, 3)

    if st.button("Submit Assessment"):

        st.session_state.depression_score = sum([q1,q2,q3,q4,q5,q6,q7,q8,q9])
        st.session_state.mania_score = sum([m1,m2,m3,m4,m5])

        st.session_state.stage = 3


elif st.session_state.stage == 3:

    st.header("Diagnosis")

    d = st.session_state.depression_score
    m = st.session_state.mania_score

    diagnosis, severity = diagnose(d, m)

    st.session_state.diagnosis = diagnosis
    st.session_state.severity = severity

    st.write("Depression Score:", d)
    st.write("Mania Score:", m)
    st.write("Diagnosis:", diagnosis)
    st.write("Severity:", severity)

    if st.button("Next"):
        st.session_state.stage = 4


elif st.session_state.stage == 4:

    st.header("Treatment")

    treatment = treatment_plan(st.session_state.diagnosis)
    st.session_state.treatment = treatment

    st.write("Diagnosis:", st.session_state.diagnosis)
    st.success("Treatment Plan:")
    st.write(treatment)

    if st.button("Next"):
        st.session_state.stage = 5


elif st.session_state.stage == 5:

    st.header("Graphs")

    d = st.session_state.depression_score
    m = st.session_state.mania_score

    fig = plt.figure()
    plt.bar(["Depression", "Mania"], [d, m])
    plt.xlabel("Type")
    plt.ylabel("Score")
    plt.title("Mood Assessment Scores")

    st.pyplot(fig)

    if st.button("Next"):
        st.session_state.stage = 6


elif st.session_state.stage == 6:

    st.header("Report")

    report = f"""
Patient Name: {st.session_state.name}
Age: {st.session_state.age}
Gender: {st.session_state.gender}

Depression Score: {st.session_state.depression_score}
Mania Score: {st.session_state.mania_score}

Diagnosis: {st.session_state.diagnosis}
Severity: {st.session_state.severity}

Treatment: {st.session_state.treatment}
"""

    st.text(report)

    st.download_button("Download Report", report)

    if st.button("Restart"):
        st.session_state.stage = 0
