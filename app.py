import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("best_churn_model.pkl")

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("📊 Customer Churn Prediction App")
st.markdown("Enter customer details below to predict churn probability.")

# --- Numeric inputs ---
age = st.number_input("Age", min_value=18, max_value=100, value=30)
avg_time_spent = st.number_input("Average Time Spent (mins)", min_value=0.0, value=10.0)
avg_transaction_value = st.number_input("Average Transaction Value", min_value=0.0, value=100.0)
avg_frequency_login_days = st.number_input("Avg Login Frequency (days)", min_value=0.0, value=5.0)
points_in_wallet = st.number_input("Points in Wallet", min_value=0.0, value=50.0)
tenure_days = st.number_input("Tenure (days)", min_value=0, value=365)

# --- Categorical inputs ---
membership = st.selectbox(
    "Membership Category", 
    ["No_Membership", "Gold_Membership", "Platinum_Membership", "Premium_Membership", "Silver_Membership"]
)
referral = st.selectbox("Joined Through Referral?", ["No", "Yes"])
offer_type = st.selectbox("Preferred Offer Type", ["Gift_Vouchers/Coupons", "Without_Offers"])
medium = st.selectbox("Medium of Operation", ["Desktop", "Smartphone"])
used_discount = st.selectbox("Used Special Discount?", ["No", "Yes"])
offer_preference = st.selectbox("Offer Application Preference?", ["No", "Yes"])
complaint_status = st.selectbox("Complaint Status", ["Not_Applicable", "Solved_in_Follow-up"])
feedback = st.selectbox(
    "Customer Feedback",
    [
        "Poor_Customer_Service", "Poor_Product_Quality", "Poor_Website",
        "Products_always_in_Stock", "Quality_Customer_Care",
        "Reasonable_Price", "Too_many_ads", "User_Friendly_Website"
    ]
)

# --- One-hot encode categorical variables ---
features = {
    "membership_category_Gold_Membership": 1 if membership == "Gold_Membership" else 0,
    "membership_category_No_Membership": 1 if membership == "No_Membership" else 0,
    "membership_category_Platinum_Membership": 1 if membership == "Platinum_Membership" else 0,
    "membership_category_Premium_Membership": 1 if membership == "Premium_Membership" else 0,
    "membership_category_Silver_Membership": 1 if membership == "Silver_Membership" else 0,
    "joined_through_referral_Yes": 1 if referral == "Yes" else 0,
    "preferred_offer_types_Gift_Vouchers/Coupons": 1 if offer_type == "Gift_Vouchers/Coupons" else 0,
    "preferred_offer_types_Without_Offers": 1 if offer_type == "Without_Offers" else 0,
    "medium_of_operation_Desktop": 1 if medium == "Desktop" else 0,
    "medium_of_operation_Smartphone": 1 if medium == "Smartphone" else 0,
    "used_special_discount_Yes": 1 if used_discount == "Yes" else 0,
    "offer_application_preference_Yes": 1 if offer_preference == "Yes" else 0,
    "complaint_status_Not_Applicable": 1 if complaint_status == "Not_Applicable" else 0,
    "complaint_status_Solved_in_Follow-up": 1 if complaint_status == "Solved_in_Follow-up" else 0,
    "feedback_Poor_Customer_Service": 1 if feedback == "Poor_Customer_Service" else 0,
    "feedback_Poor_Product_Quality": 1 if feedback == "Poor_Product_Quality" else 0,
    "feedback_Poor_Website": 1 if feedback == "Poor_Website" else 0,
    "feedback_Products_always_in_Stock": 1 if feedback == "Products_always_in_Stock" else 0,
    "feedback_Quality_Customer_Care": 1 if feedback == "Quality_Customer_Care" else 0,
    "feedback_Reasonable_Price": 1 if feedback == "Reasonable_Price" else 0,
    "feedback_Too_many_ads": 1 if feedback == "Too_many_ads" else 0,
    "feedback_User_Friendly_Website": 1 if feedback == "User_Friendly_Website" else 0
}

# Put all features in the right order
input_data = [
    age, avg_time_spent, avg_transaction_value, avg_frequency_login_days,
    points_in_wallet, tenure_days,
    *features.values()
]

# Predict
if st.button("🔮 Predict Churn"):
    prediction = model.predict([input_data])[0]
    prob = model.predict_proba([input_data])[0][1]  # Probability of churn
    
    if prediction == 1:
        st.error(f"⚠️ This customer is **likely to churn**. Probability: {prob:.2f}")
    else:
        st.success(f"✅ This customer is **not likely to churn**. Probability: {prob:.2f}")
