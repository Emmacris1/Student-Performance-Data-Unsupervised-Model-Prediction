import streamlit  as st
import pandas as pd
import numpy as np
import joblib

st.title('Student Performance Clustering')
st.write('Developed by Ima')

st.sidebar.markdown('Inputs')
Age = st.sidebar.number_input('Enter Age',value=18)
Gender = st.sidebar.number_input('Enter Gender')
Ethnicity = st.sidebar.number_input('Enter Ethnicity')
ParentalEducation = st.sidebar.number_input('Enter ParentalEducation')
StudyTimeWeekly = st.sidebar.number_input('Enter StudyTimeWeekly')
Absences = st.sidebar.number_input('Enter Absences')
Tutoring = st.sidebar.number_input('Enter Tutoring')
ParentalSupport = st.sidebar.number_input('Enter ParentalSupport')
ExtraCurricular = st.sidebar.number_input('Enter ExtraCurricular')
Sports = st.sidebar.number_input('Enter Sports')
Music = st.sidebar.number_input('Enter Music')
Volunteering = st.sidebar.number_input('Enter Volunteering')
GPA = st.sidebar.number_input('Enter GPA')
GradeClass = st.sidebar.number_input('Enter GradeClass')

inputs = np.array([Age, Gender, Ethnicity, ParentalEducation, StudyTimeWeekly,
       Absences, Tutoring, ParentalSupport, ExtraCurricular, Sports,
       Music, Volunteering, GPA, GradeClass]).reshape(1,-1)

scaler = joblib.load('mystandard_scaler.pkl')
x_scale = scaler.transform(inputs)
model = joblib.load('kmeans.pkl')


if st.button('Predict'):
    result = model.predict(x_scale)
    st.write(result)

