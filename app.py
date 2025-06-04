import streamlit as st

st.title("Interest Calculator")

tab1, tab2 = st.tabs(["Simple Interest", "Compound Interest"])

with tab1:
    st.subheader("Simple Interest Calculator")
    with st.form("interest_form"):
        principal = st.number_input("Principal Amount", min_value=0.0, step=100.0)
        rate = st.number_input("Rate of Interest (%)", min_value=0.0, step=0.1)
        time = st.number_input("Time (years)", min_value=0, step=1)

        calculate_button = st.form_submit_button("Calculate Interest")
        if calculate_button:
            interest = (principal * rate * time) / 100
            st.success(f"The calculated interest is: {interest:.2f}")


with tab2:
    st.subheader("Compound Interest Calculator")
    with st.form("compound_interest_form"):
        principal = st.number_input("Principal Amount", min_value=0.0, step=100.0)
        rate = st.number_input("Rate of Interest (%)", min_value=0.0, step=0.1)
        time = st.number_input("Time (years)", min_value=0, step=1)
        col1, col2 = st.columns(2)
        with col1:
            compounding_frequency = st.selectbox("Compounding Frequency", ["Yearly", "Half-Yearly", "Quarterly", "Monthly"])
        with col2:
            compounding_frequency = st.selectbox("Compounding sFrequency", ["Yearly", "Half-Yearly", "Quarterly", "Monthly"])
        

        calculate_button = st.form_submit_button("Calculate Compound Interest")
        if calculate_button:
            if compounding_frequency == "Yearly":
                n = 1
            elif compounding_frequency == "Half-Yearly":
                n = 2
            elif compounding_frequency == "Quarterly":
                n = 4
            else:  # Monthly
                n = 12

            amount = principal * (1 + (rate / (n * 100))) ** (n * time)
            compound_interest = amount - principal
            st.success(f"The calculated compound interest is: {compound_interest:.2f}")
