Student Performance Clustering with K-Means
Overview

This project uses unsupervised machine learning to cluster students based on academic performance, study habits, and extracurricular activities. The model was deployed with Streamlit to provide an interactive prediction interface.

Features
Student data clustering using K-Means
Data preprocessing with StandardScaler
Interactive web app built with Streamlit
Real-time cluster prediction
Behavioral and academic pattern analysis
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib
Project Structure
├── app.py
├── Unsupervised Learning.ipynb
├── kmeans.pkl
├── mystandard_scaler.pkl
└── README.md
How It Works
User inputs student-related information:
Age
GPA
Study time
Absences
Tutoring
Extracurricular activities
And more
The input data is standardized using a trained scaler.
The K-Means model predicts the student's cluster group.
The result is displayed through the Streamlit interface.
Installation

Clone the repository:

git clone https://github.com/yourusername/student-performance-clustering.git

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py
Future Improvements
Add cluster visualization dashboards
Improve UI/UX design
Add model evaluation metrics
Deploy online using Streamlit Cloud or Render
Author

Developed by Ima
