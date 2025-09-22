import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Marks Analysis", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #f9fbfd;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
    }
    h1, h2, h3, h4 {
        color: #1e3a8a; /* Dark Blue */
    }
    .stDataFrame {
        border: 2px solid #1e40af;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Student Marks Analysis Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df, use_container_width=True)

    # Student-wise Performance

    st.subheader("Student-wise Performance")
    col1, col2 = st.columns([1, 2])

    with col1:
        student_names = df["Name"].tolist()
        selected_student = st.selectbox("Select a student", student_names)

    student_data = df[df["Name"] == selected_student].T
    student_data = student_data.drop(["Student_ID", "Name", "Class"])
    student_data.columns = ["Marks"]

    with col2:
        st.write(f"Performance of **{selected_student}**")
        st.dataframe(student_data)

        # Bar Plot
        fig, ax = plt.subplots(figsize=(6, 4))
        student_data.plot(kind="bar", legend=False, ax=ax, color="#3b82f6")  # Blue
        plt.ylabel("Marks")
        plt.title(f"{selected_student}'s Marks", color="#1e3a8a")
        st.pyplot(fig)


    # Subject Averages

    st.subheader("Subject Averages")
    subject_cols = ["Math", "Science", "English", "Social", "Computer"]
    subject_averages = df[subject_cols].mean()

    col3, col4 = st.columns([1, 2])
    with col3:
        st.write(subject_averages)

    with col4:
        fig, ax = plt.subplots(figsize=(6, 4))
        subject_averages.plot(kind="bar", color="#60a5fa", ax=ax)  # Light Blue
        plt.ylabel("Average Marks")
        plt.title("Subject Averages", color="#1e3a8a")
        st.pyplot(fig)


    # Highest & Lowest Scores

    st.subheader("Highest & Lowest Scores")
    highest_scores = df[subject_cols].max()
    lowest_scores = df[subject_cols].min()

    col5, col6 = st.columns(2)
    with col5:
        st.write("### 🟦 Highest Scores")
        st.dataframe(highest_scores)

    with col6:
        st.write("### 🟦 Lowest Scores")
        st.dataframe(lowest_scores)


    # Search Student

    st.subheader("Search Student")
    search_query = st.text_input("Enter student name to search")

    if search_query:
        result = df[df["Name"].str.contains(search_query, case=False, na=False)]
        if not result.empty:
            st.write("Search Results:")
            st.dataframe(result, use_container_width=True)
        else:
            st.warning("No student found with that name.")
else:
    st.info("Please upload a CSV file to proceed.")
