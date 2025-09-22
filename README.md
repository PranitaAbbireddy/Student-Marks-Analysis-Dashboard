# Student Marks Analysis Dashboard

This project is a Streamlit web application designed to help teachers and students visualize and analyze academic performance from a CSV dataset. It provides an interactive dashboard where users can upload student marks data and gain insights into performance at both the individual and subject level.

## Features

- Upload a CSV file containing student details and marks
- View student-wise performance in both table and chart formats
- Calculate and visualize subject averages
- Display the highest and lowest scores in each subject
- Search functionality to find a particular student quickly
- Clean and minimal interface in blue and white theme for easy readability

## Technologies Used

- Python  
- Streamlit  
- Pandas  
- Matplotlib

## How to Run the Project

1. **Clone the repository** to your local machine:
   
     git clone https://github.com/your-username/student-marks-analysis-dashboard.git
     cd student-marks-analysis-dashboard
   
2. **Create and activate a virtual environment**:

    python -m venv venv
    venv\Scripts\activate       # Windows
    source venv/bin/activate    # macOS/Linux

3. **Install the required dependencies**:

    pip install -r requirements.txt

4. **Run the Streamlit application**:

    streamlit run app.py

5. **Open the local URL** displayed in your terminal (usually http://localhost:8501).

- Upload a CSV file containing student marks (a sample dataset students_marks.csv is already included).

6. **Explore the dashboard**:

- View student-wise performance
- Check subject averages
- See highest and lowest scores
- Use the search filter to find a student quickly

