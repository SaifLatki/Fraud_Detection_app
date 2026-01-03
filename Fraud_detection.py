import streamlit as st
import pandas as pd
import joblib


# ================= Page Config =================
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="wide",
)

# ================= Load Model =================
model = joblib.load("fraud_detection_pipline.pkl")


# ================= Custom CSS =================
st.markdown("""
<style>
/* App background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #020617, #0f172a);
    color: #f8fafc;
}

/* Remove default header */
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
    border-right: 1px solid #1e293b;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    padding: 2rem;
    border-radius: 22px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    margin-bottom: 1.5rem;
}

/* Titles */
.title {
    font-size: 2.8rem;
    font-weight: 800;
    color: #38bdf8;
}
.subtitle {
    font-size: 1.15rem;
    color: #c7d2fe;
}

/* Section heading */
.section {
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    border: none;
    border-radius: 16px;
    padding: 0.9rem;
    font-size: 1.1rem;
    font-weight: 700;
    color: white;
    transition: 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.04);
    background: linear-gradient(135deg, #1e40af, #5b21b6);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #9ca3af;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)


# ================= Sidebar =================
with st.sidebar:
    st.markdown("## 💳 Fraud Detection")
    st.markdown(
        """
        **AI-powered financial security system**

        🔐 Secure Transactions  
        ⚡ Real-time Prediction  
        🧠 Machine Learning Model  

        ---
        **Use Case**
        - Banking systems  
        - Payment gateways  
        - FinTech platforms  
        """
    )


# ================= Main Layout =================
st.markdown("<div class='title'>Fraud Detection System</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Detect suspicious financial transactions instantly using AI</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ================= Input Section =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section'>🔍 Transaction Information</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    transaction_type = st.selectbox(
        "Transaction Type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
    )
    amount = st.number_input("Amount", min_value=0.0, value=5000.0, step=500.0)

with col2:
    oldbalanceOrg = st.number_input("Sender Old Balance", min_value=0.0, value=10000.0)
    newbalanceOrig = st.number_input("Sender New Balance", min_value=0.0, value=9000.0)

with col3:
    oldbalanceDest = st.number_input("Receiver Old Balance", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("Receiver New Balance", min_value=0.0, value=0.0)

st.markdown("</div>", unsafe_allow_html=True)


# ================= Prediction Section =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section'>🧠 AI Risk Assessment</div>", unsafe_allow_html=True)

if st.button("🚀 Analyze Transaction"):
    with st.spinner("Analyzing transaction pattern..."):
        input_data = pd.DataFrame({
            "type": [transaction_type],
            "amount": [amount],
            "oldbalanceOrg": [oldbalanceOrg],
            "newbalanceOrig": [newbalanceOrig],
            "oldbalanceDest": [oldbalanceDest],
            "newbalanceDest": [newbalanceDest]
        })

        prediction = model.predict(input_data)

        st.markdown("<br>", unsafe_allow_html=True)

        if prediction[0] == 1:
            st.error("🚨 **High Risk Detected**   This transaction is **likely fraudulent**.")
        else:
            st.success("✅ **Transaction Approved**  No fraud patterns detected.")

st.markdown("</div>", unsafe_allow_html=True)


# ================= Footer =================
st.markdown(
    "<div class='footer'>© 2025 Fraud Detection System · Secure • Intelligent • Reliable</div>",
    unsafe_allow_html=True
)
