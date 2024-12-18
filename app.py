import streamlit as st

pages = {
    "Linear Regression": [
        st.Page("LinearRegression/advertising-sales-prediction.py", title="Advertising Sales Prediction")
    ],
    "Logistic Regression": [
        st.Page("LogisticRegression/later.py", title="TBD")
    ]
}

selected_page = st.navigation(pages)
selected_page.run()
