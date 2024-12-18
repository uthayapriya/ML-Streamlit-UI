from LinearRegression.utils import predict_sales, validate_input
import streamlit as st

st.title("Linear Regression")
st.markdown("This model was trained using **Ridge** regression with a dummy dataset. Development was done only for practising my ML skills using scikit-learn.")
st.markdown("<hr />", unsafe_allow_html=True)
st.markdown("<h2>Advertisment Sales Prediction</h2>", unsafe_allow_html=True)
st.markdown("Amount spent on TV, Radio and Newspaper Ads are the independent parameters. The final sales value is the dependent value.")

st.markdown("<br />", unsafe_allow_html=True)
st.write("Please enter the amount spent for different advertising methods")

if not 'submitted' in st.session_state:
    st.session_state.submitted = False

tv_spent = st.text_input("Amount spent in **$** for TV Ads")
radio_spent = st.text_input("Amount spent in **$** for Radio Ads")
newspaper_spent = st.text_input("Amount spent in **$** for Newspaper Ads")

st.session_state.submitted = st.button("Submit", type="primary")

if st.session_state.submitted:
    parameters = [tv_spent, radio_spent, newspaper_spent]
    if not all(parameters):
        st.error("Please enter values for all inputs")
        st.stop()

    result = validate_input(parameters)
    if not result:
        st.error("Please enter valid input")
        st.stop()

    predicted_sales = predict_sales(parameters=result)
    st.write(f"By spending the following")
    st.write(f"**${tv_spent}** on TV Ads")
    st.write(f"**${radio_spent}** on Radio Ads")
    st.write(f"**${newspaper_spent}** on Newspaper Ads")
    st.write(f"You can approximately make a sales value of **${round(predicted_sales, 2)} Million**")