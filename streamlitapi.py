import pickle 
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning)  # suppress sklearn warnings



# Load the trained model
model = pickle.load(open(
    r'C:/Users/manas/OneDrive/Documents/DATA SCIENCE/ML PROJECTS/STARTUP PREDICTION/Startup_Prediction_Classifier.pkl', 
    'rb'))

def main():
    st.title("🚀 STARTUP SUCCESS PREDICTION")

    # Create a form
    with st.form("prediction_form"):
        st.subheader("Enter Startup Information")

        # Numerical inputs
        age_first_funding_year = st.number_input("Age at First Funding Year", min_value=0)
        age_last_funding_year = st.number_input("Age at Last Funding Year", min_value=0)
        funding_total_usd = st.number_input("Total Funding (USD)", min_value=0.0)
        avg_participants = st.number_input("Average Participants", min_value=0.0)

        # Categorical inputs
        # name = st.text_input("Startup Name")
        # labels = st.text_input("Labels")
        relationships = st.number_input("Relationships", min_value=0)
        funding_rounds = st.number_input("Number of Funding Rounds", min_value=0)
        milestones = st.number_input("Milestones", min_value=0)

        # is_CA = st.selectbox("Is in California?", ["Yes", "No"])
        # is_NY = st.selectbox("Is in New York?", ["Yes", "No"])
        # is_MA = st.selectbox("Is in Massachusetts?", ["Yes", "No"])
        # is_TX = st.selectbox("Is in Texas?", ["Yes", "No"])
        # is_otherstate = st.selectbox("Is in Other State?", ["Yes", "No"])

        category_code = st.selectbox("Category", [
            "software", "web", "mobile", "enterprise", "advertising",
            "gamesvideo", "ecommerce", "biotech", "consulting", "other"
        ])

        is_software = st.selectbox("Software Startup?", ["Yes", "No"])
        is_web = st.selectbox("Web-based?", ["Yes", "No"])
        is_mobile = st.selectbox("Mobile-based?", ["Yes", "No"])
        is_enterprise = st.selectbox("Enterprise Startup?", ["Yes", "No"])
        is_advertising = st.selectbox("Advertising?", ["Yes", "No"])
        is_gamesvideo = st.selectbox("Games/Video?", ["Yes", "No"])
        is_ecommerce = st.selectbox("E-commerce?", ["Yes", "No"])
        is_biotech = st.selectbox("Biotech?", ["Yes", "No"])
        is_consulting = st.selectbox("Consulting?", ["Yes", "No"])
        is_othercategory = st.selectbox("Other Category?", ["Yes", "No"])

        has_VC = st.selectbox("Has VC Funding?", ["Yes", "No"])
        has_angel = st.selectbox("Has Angel Investment?", ["Yes", "No"])
        has_roundA = st.selectbox("Has Series A?", ["Yes", "No"])
        has_roundB = st.selectbox("Has Series B?", ["Yes", "No"])
        has_roundC = st.selectbox("Has Series C?", ["Yes", "No"])
        has_roundD = st.selectbox("Has Series D?", ["Yes", "No"])
        is_top500 = st.selectbox("Is in Top 500 Startups?", ["Yes", "No"])

        # Submit button inside the form
        submitted = st.form_submit_button("Predict")

    # Prediction logic after form is submitted
    if submitted:
        def yesno(val): return 1 if val == "Yes" else 0

        input_data = [
            relationships, funding_rounds, age_first_funding_year,
            age_last_funding_year, funding_total_usd, milestones,
            # yesno(is_CA), yesno(is_NY), yesno(is_MA), yesno(is_TX), yesno(is_otherstate),
            category_code, yesno(is_software), yesno(is_web), yesno(is_mobile),
            yesno(is_enterprise), yesno(is_advertising), yesno(is_gamesvideo),
            yesno(is_ecommerce), yesno(is_biotech), yesno(is_consulting),
            yesno(is_othercategory), yesno(has_VC), yesno(has_angel),
            yesno(has_roundA), yesno(has_roundB), yesno(has_roundC),
            yesno(has_roundD), avg_participants, yesno(is_top500)
        ]

        # Run prediction
        prediction = model.predict([input_data])[0]
        st.success(f"✅ Predicted Startup Status: **{prediction}**")

if __name__ == "__main__":
    main()
