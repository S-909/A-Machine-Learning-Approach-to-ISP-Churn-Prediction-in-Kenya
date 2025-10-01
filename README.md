# A Machine Learning Approach to ISP Churn Prediction in Kenya

## Dataset  
This project uses a CSV dataset containing 36,992 customer records, each with 23 features.

## Key Target Variable  
The target variable is **'churn'**, indicating whether a customer has churned (Yes/No), defined as 30 days of inactivity or cancellation.

## Objectives  
- Predict customer churn risk with a recall of at least 70% to accurately identify high-risk customers.  
- Identify the main factors driving churn at both global and segment levels.  
- Integrate customer feedback and sentiment analysis into the predictive features.  
- Propose actionable strategies to reduce churn by at least 10% year-over-year.

## Business Benefits  
- **Lower Acquisition Costs:** Retaining existing customers is approximately five times cheaper than acquiring new ones.  
- **Increased Customer Lifetime Value (CLV):** Targeted offers help extend customer loyalty and lifetime.  
- **Customer-Centric Innovation:** Analyzing complaints and sentiment drives improvements in products and services.  
- **Revenue Stability:** Early detection of churn enables proactive retention efforts.

# Methodology

## 1. Business Understanding  
- Defined churn as customers inactive for 30+ days or who have canceled.  
- Identified key performance indicators: retention rate and customer lifetime value (CLV).  
- Set success criteria: the predictive model must achieve at least 70% recall on churned customers.

## 2. Data Understanding  
- Conducted descriptive statistics to analyze data distribution and detect outliers.  
- Performed missing value analysis to identify and address data gaps.  
- Merged all datasets using a unified `customer_id` key to ensure consistency.

## 3. Data Preprocessing & Feature Engineering  
- **Missing Values:** Dropped less than 1.7% of rows due to missing data, which was negligible.  
- **Standardization:** Centered and scaled continuous variables for uniformity.  
- **Normalization:** Rescaled skewed features such as average session length.  
- **Encoding:** Applied one-hot encoding for nominal variables and ordinal encoding for membership tiers.  
- **Feature Creation:** Added new features including complaint-resolution latency, rolling 30-day login frequency, and sentiment scores derived from VADER.

## 4. Modeling  
Evaluated five machine learning models:  
1. Logistic Regression (baseline)  
2. Random Forest (interpretable and robust)  
3. XGBoost (best overall performance with ROC-AUC of 0.94 and recall of 0.85)  
4. LightGBM (fast and memory-efficient)  
5. Multi-Layer Perceptron (MLP) using Keras (captures non-linear patterns)

## 5. Evaluation & Interpretation  
- Used confusion matrices to assess true/false positives and negatives.  
- Measured ROC-AUC to evaluate the model’s ability to distinguish churners from non-churners.  
- Analyzed precision-recall curves to handle class imbalance and balance precision with recall.  
- Applied SHAP values to identify and visualize the most influential features driving churn predictions.

## Exploratory Data Analysis Highlights  
- Churn rate is highest among Basic members at 27%, compared to 8% for Gold members.  
- Customers who file complaints are twice as likely to churn, even if issues are resolved within SLA.  
- Wallet engagement (points earned and redeemed) negatively correlates with churn (Pearson correlation = -0.47).  
- Urban customers churn 1.6 times more than suburban customers, likely due to increased competition.

## Key Insights & Recommendations  
- **Upgrade Incentives:** Provide tiered discounts to encourage Basic members to upgrade to Silver within their first 90 days.  
- **Complaint Concierge:** Establish a dedicated “white-glove” resolution team for high-value accounts.  
- **Dynamic Loyalty Points:** Gamify wallet usage with streak bonuses and badges to boost engagement.  
- **Geo-Targeted Retention:** Focus retention advertising on metro areas with high churn rates.  
- **Early-Warning Triggers:** Automate retention offers when churn probability exceeds 0.65 and loyalty engagement falls below 10 points per month.