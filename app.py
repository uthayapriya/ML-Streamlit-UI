import streamlit as st

pages = {
    "Linear Regression": [
        st.Page("LinearRegression/advertising-sales-prediction.py", title="Advertising Sales Prediction")
    ],
    "Logistic Regression": [
        st.Page("LogisticRegression/airline-satisfaction.py", title="Airline Satisfaction Prediction")
    ],
    "Support Vector Machines": [
        st.Page("SVM/soon.py", title="Soon")
    ]
}

selected_page = st.navigation(pages)
selected_page.run()
