import streamlit as st
import joblib

# Load the saved model
model = joblib.load("best_churn_model.pkl")

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.image("pic-logo.jpeg", width=100)

st.title("Customer Churn Prediction App")
st.markdown("Enter customer details below to predict churn probability.")

# --- Numeric inputs ---
points_in_wallet = st.number_input("Points in Wallet", min_value=0.0, value=50.0)
avg_transaction_value = st.number_input("Average Transaction Value", min_value=0.0, value=100.0)
tenure_days = st.number_input("Tenure (days)", min_value=0, value=365)
avg_time_spent = st.number_input("Average Time Spent (mins)", min_value=0.0, value=10.0)
avg_frequency_login_days = st.number_input("Avg Login Frequency (days)", min_value=0.0, value=5.0)

# --- Membership Category ---
membership = st.selectbox(
    "Membership Category", 
    ["No_Membership", "Gold_Membership", "Platinum_Membership", "Premium_Membership", "Silver_Membership"]
)

# --- Feedback ---
feedback = st.selectbox(
    "Customer Feedback",
    [
        "Poor_Customer_Service", "Poor_Product_Quality", "Poor_Website",
        "Products_always_in_Stock", "Quality_Customer_Care",
        "Reasonable_Price", "Too_many_ads", "User_Friendly_Website"
    ]
)

# --- Medium of Operation ---
medium = st.selectbox("Medium of Operation", ["Desktop", "Smartphone"])

# --- Offer Application Preference ---
offer_preference = st.selectbox("Offer Application Preference?", ["No", "Yes"])

# --- Referral ---
referral = st.selectbox("Joined Through Referral?", ["No", "Yes"])

# --- Complaint Status ---
complaint_status = st.selectbox("Complaint Status", ["Not_Applicable", "Solved_in_Follow-up"])

# --- Preferred Offer Type ---
offer_type = st.selectbox("Preferred Offer Type", ["Gift_Vouchers/Coupons", "Without_Offers"])

# --- Used Special Discount ---
used_discount = st.selectbox("Used Special Discount?", ["No", "Yes"])

# --- One-hot encode categorical variables ---
features = [
    points_in_wallet,
    avg_transaction_value,
    tenure_days,
    avg_time_spent,
    avg_frequency_login_days,
    1 if membership == "Gold_Membership" else 0,
    1 if membership == "No_Membership" else 0,
    1 if membership == "Platinum_Membership" else 0,
    1 if membership == "Premium_Membership" else 0,
    1 if membership == "Silver_Membership" else 0,
    1 if referral == "Yes" else 0,
    1 if offer_type == "Gift_Vouchers/Coupons" else 0,
    1 if offer_type == "Without_Offers" else 0,
    1 if medium == "Desktop" else 0,
    1 if medium == "Smartphone" else 0,
    1 if used_discount == "Yes" else 0,
    1 if offer_preference == "Yes" else 0,
    1 if complaint_status == "Not_Applicable" else 0,
    1 if complaint_status == "Solved_in_Follow-up" else 0,
    1 if feedback == "Poor_Customer_Service" else 0,
    1 if feedback == "Poor_Product_Quality" else 0,
    1 if feedback == "Poor_Website" else 0,
    1 if feedback == "Products_always_in_Stock" else 0,
    1 if feedback == "Quality_Customer_Care" else 0,
    1 if feedback == "Reasonable_Price" else 0,
    1 if feedback == "Too_many_ads" else 0,
    1 if feedback == "User_Friendly_Website" else 0
]

if st.button("🔮 Predict Churn"):
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1]
    if prediction == 1:
        st.error(f"⚠️ This customer is **likely to churn**. Probability: {prob:.2f}")
    else:
        st.success(f"✅ This customer is **not likely to churn**. Probability: {prob:.2f}")
