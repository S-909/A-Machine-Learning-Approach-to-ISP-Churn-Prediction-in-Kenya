import streamlit as st
import joblib

# Load the saved model
model = joblib.load("best_churn_model.pkl")

# Page config
st.set_page_config(
    page_title="ISP Churn Prediction Platform", 
    layout="wide"
    
)

# Custom CSS to match landing page theme
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding: 3rem 2rem;
        max-width: 2000px;
    }
    
    /* Header section */
    .header-container {
        text-align: center;
        color: white;
        margin-bottom: 3rem;
        animation: fadeIn 0.8s ease-in;
    }
    
    .header-container h1 {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
    }
    
    .header-container p {
        font-size: 1.2rem;
        opacity: 0.95;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .prediction-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
        animation: slideUp 0.6s ease-out;
    }
    
    .section-header {
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    /* Input styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Labels */
    .stNumberInput > label,
    .stSelectbox > label {
        color: white;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        border: none;
        font-weight: 700;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        margin-top: 2rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
    }
    
    /* Success/Error boxes */
    .stAlert {
        border-radius: 15px;
        padding: 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        animation: popIn 0.5s ease-out;
    }
    
    /* Stats grid */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 3rem;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: #718096;
        font-weight: 500;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideUp {
        from { 
            opacity: 0;
            transform: translateY(30px);
        }
        to { 
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes popIn {
        0% { 
            opacity: 0;
            transform: scale(0.8);
        }
        100% { 
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Logo styling */
    img {
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        margin-bottom: 1rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header

st.markdown("""
<div class="header-container">
    <h1>🔮 Customer Churn Prediction</h1>
    <p>Enter customer details below to get instant AI-powered churn probability predictions</p>
</div>
""", unsafe_allow_html=True)

# Stats section
st.markdown("""

""", unsafe_allow_html=True)

# Main prediction form

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 class="section-header">📊 Customer Metrics</h3>', unsafe_allow_html=True)
    points_in_wallet = st.number_input("Points in Wallet", min_value=0.0, value=50.0, help="Loyalty points balance")
    avg_transaction_value = st.number_input("Average Transaction Value", min_value=0.0, value=100.0, help="Average spend per transaction")
    tenure_days = st.number_input("Tenure (days)", min_value=0, value=365, help="Days as customer")
    avg_time_spent = st.number_input("Average Time Spent (mins)", min_value=0.0, value=10.0, help="Avg session duration")
    avg_frequency_login_days = st.number_input("Avg Login Frequency (days)", min_value=0.0, value=5.0, help="Days between logins")

with col2:
    st.markdown('<h3 class="section-header">👤 Customer Profile</h3>', unsafe_allow_html=True)
    membership = st.selectbox(
        "Membership Category", 
        ["No_Membership", "Gold_Membership", "Platinum_Membership", "Premium_Membership", "Silver_Membership"],
        help="Current membership tier"
    )
    
    medium = st.selectbox("Medium of Operation", ["Desktop", "Smartphone"], help="Primary device used")
    
    referral = st.selectbox("Joined Through Referral?", ["No", "Yes"], help="Referred by existing customer")
    
    offer_preference = st.selectbox("Offer Application Preference?", ["No", "Yes"], help="Opts in for offers")
    
    used_discount = st.selectbox("Used Special Discount?", ["No", "Yes"], help="Has used discounts")

# Full width inputs
st.markdown('<h3 class="section-header">💬 Feedback & Support</h3>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    feedback = st.selectbox(
        "Customer Feedback",
        [
            "Poor_Customer_Service", "Poor_Product_Quality", "Poor_Website",
            "Products_always_in_Stock", "Quality_Customer_Care",
            "Reasonable_Price", "Too_many_ads", "User_Friendly_Website"
        ],
        help="Most recent feedback sentiment"
    )
    
    complaint_status = st.selectbox(
        "Complaint Status", 
        ["Not_Applicable", "Solved_in_Follow-up"],
        help="Customer complaint history"
    )

with col4:
    offer_type = st.selectbox(
        "Preferred Offer Type", 
        ["Gift_Vouchers/Coupons", "Without_Offers"],
        help="Offer preference type"
    )

# One-hot encode categorical variables
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

# Prediction button
if st.button("🔮 Predict Churn Probability"):
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ **HIGH CHURN RISK** - This customer is likely to churn with {prob:.2f} probability")
        st.markdown("""
        **Recommended Actions:**
        - Reach out proactively with retention offers
        - Address any outstanding complaints immediately
        - Consider membership tier upgrade incentives
        """)
    else:
        st.success(f"✅ **LOW CHURN RISK** - This customer is likely to stay with {(1-prob):.2f}% retention probability")
        st.markdown("""
        **Recommended Actions:**
        - Continue current engagement strategies
        - Consider upselling opportunities
        - Maintain quality service standards
        """)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem; opacity: 0.9;">
    
</div>
""", unsafe_allow_html=True)