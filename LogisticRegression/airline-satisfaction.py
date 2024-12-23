import streamlit as st

st.title("Logistic Regression")

st.write("This model was trained using **Logistic Regression** with a dummy dataset. Development was done only for practising my ML skills using scikit-learn.")

st.markdown("<hr />", unsafe_allow_html=True)

st.markdown("<h2>Airline Satisfaction Prediction</h2>", unsafe_allow_html=True)

st.write("Following were the steps taken to train the model:")
st.write("1. **Data Cleaning**: Checked for missing values, replaced them with the appropriate value.")
st.write("2. **Exploratory Data Analysis**: Checked for the distribution of the data.")
st.write("3. **Data Preprocessing**: Converted categorical data into numerical data. Encoded target with Label Encoder and categorical values with One Hot Encoding.")
st.write("4. **Model Training**: Used Logistic Regression to train the model.")
st.write("5. **Model Evaluation**: Evaluated the model using confusion matrix and classification report.")

st.markdown("<br />", unsafe_allow_html=True)

st.write("Github Repository: <a href='https://github.com/muhdjawad03/flight-satisfaction'>Airline Satisfaction Prediction</a>", unsafe_allow_html=True)