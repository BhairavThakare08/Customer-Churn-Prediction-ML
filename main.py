import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import pandas as pd

# ================= LOAD MODEL =================
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

/* ===== MAIN BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0B0F19, #111827);
    color: #E6EDF3;
}

/* ===== HEADER ===== */
.header {
    background: linear-gradient(90deg, #1f3c88, #0f2027);
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.6);
}

/* ===== CARD ===== */
.card {
    background: linear-gradient(145deg, #111827, #1f2937);
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 25px rgba(0,0,0,0.6);
    border: 1px solid #1f2937;
}

/* ===== TEXT ===== */
h1, h2, h3, h4, h5, h6, p, label {
    color: #E6EDF3 !important;
}

/* ===== INPUT BOX ===== */
textarea, input, select {
    background-color: #020617 !important;
    color: #E6EDF3 !important;
    border-radius: 8px !important;
    border: 1px solid #1f2937 !important;
}

/* ===== SELECT BOX FIX ===== */
div[data-baseweb="select"] > div {
    background-color: #020617 !important;
    color: #E6EDF3 !important;
}

/* ===== SLIDER ===== */
.stSlider > div {
    color: white !important;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    height: 50px;
    border-radius: 10px;
    font-size: 18px;
    border: none;
}

/* Hover */
.stButton>button:hover {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
}

/* ===== SUCCESS / ERROR ===== */
.stAlert {
    background: linear-gradient(90deg, #134E4A, #166534) !important;
    border-radius: 10px;
}

/* ===== CHART BACKGROUND FIX ===== */
.css-1kyxreq, .css-1v0mbdj {
    background-color: transparent !important;
}

/* REMOVE WHITE BLOCK */
.block-container {
    background-color: transparent !important;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="header">
<h1>Customer Churn <span style='color:orange'>Prediction</span></h1>
</div>
""", unsafe_allow_html=True)

# ================= LAYOUT =================
left, right = st.columns([1,2])

# ================= LEFT PANEL =================
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Customer Input")

    gender = st.selectbox("Gender", ["Male","Female"])
    senior = st.selectbox("Senior Citizen", ["No","Yes"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

    monthly = st.slider("Monthly Charges", 0, 150, 70)
    total = st.number_input("Total Charges", 0)

    contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
    internet = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])
    tech = st.selectbox("Tech Support", ["No","Yes"])
    security = st.selectbox("Online Security", ["No","Yes"])

    predict_btn = st.button("Predict Churn 🚀")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= ENCODING =================
gender = 1 if gender=="Female" else 0
senior = 1 if senior=="Yes" else 0
tech = 1 if tech=="Yes" else 0
security = 1 if security=="Yes" else 0

contract_map = {"Month-to-month":0,"One year":1,"Two year":2}
internet_map = {"DSL":0,"Fiber optic":1,"No":2}

contract = contract_map[contract]
internet = internet_map[internet]

# ================= SCALE NUMERIC =================
num_data = np.array([[tenure, monthly, total]])
num_scaled = scaler.transform(num_data)

# ================= FINAL INPUT =================
final_input = np.array([[
    gender,
    num_scaled[0][0],
    num_scaled[0][1],
    num_scaled[0][2],
    contract,
    internet,
    tech,
    security,
    senior
]])

# ================= RIGHT PANEL =================
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Prediction Result")

    if predict_btn:

        pred = model.predict(final_input)[0]
        prob = model.predict_proba(final_input)[0][1]

        # 🔴 Prediction Box
        if pred == 1:
            st.error("⚠️ Churn Likely")
        else:
            st.success("✅ Customer Will Stay")

        # ================= LAYOUT =================
        col_chart, col_info = st.columns([2,1])

        # ================= DONUT CHART =================
        with col_chart:
            st.write("### Churn Probability")

            fig, ax = plt.subplots()

            ax.pie(
                [prob, 1-prob],
                labels=["Churn", "Non-Churn"],
                autopct='%1.1f%%',
                colors=["#ff3c00", "#4a4ad1"],
                startangle=90
            )

            # donut hole
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig.gca().add_artist(centre_circle)

            ax.text(0, 0, f"{int(prob*100)}%", ha='center', va='center', fontsize=24)

            st.pyplot(fig)

        # ================= SIDE INFO =================
        with col_info:

            # 🔥 Key Features
            st.markdown("### Key Features")
            if monthly > 80:
                st.write("• High Monthly Charges")
            if internet == 1:
                st.write("• Fiber Optic Internet")
            if contract == 0:
                st.write("• Month-to-month Contract")
            if tech == 0:
                st.write("• No Tech Support")

            # 🔥 Model Performance
            st.markdown("### Model Performance")
            st.write("✅ Accuracy: 74%")
            st.write("🟠 F1 Score: 0.62")
            st.write("🟢 Recall: 0.81")

            # ================= ADD HERE =================
            st.markdown("### 📉 Churn Risk Factors")

            import pandas as pd

            risk_data = pd.DataFrame({
                "Factor": ["Monthly Charges", "Contract Type", "Tech Support", "Online Security"],
                "Risk Score": [
                    monthly/150,
                    1 if contract == 0 else 0.3,
                    1 if tech == 0 else 0.2,
                    1 if security == 0 else 0.2
                ]
            })

            st.bar_chart(risk_data.set_index("Factor"))

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("🚀 Built by Bhairav | ML Churn Prediction Project")