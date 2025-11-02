import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

# ============ LOAD MODEL ============
model = pkl.load(open('model.pkl', 'rb'))

# ============ PAGE CONFIG ============
st.set_page_config(page_title='Diabetes Diagnosis App', page_icon="💉", layout='centered')

# ============ PAGE DESIGN ============
st.markdown("""
    <style>
    /* Background gradient */
    [class*="stAppViewContainer"] {
        background: linear-gradient(120deg, #b3e5fc, #ffffff);
    }

    /* Main content box styling */
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Button design */
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s;
        border: none;
    }

    .stButton>button:hover {
        background-color: #004c99;
        color: #ffffff;
        transform: scale(1.03);
    }

    /* Input field design */
    .stNumberInput>div>div>input {
        border: 1px solid #0078ff !important;
        color: #000000 !important;
        background-color: #f9f9f9;
    }

    /* Text and headings */
    h1, h2, h3, label, .stMarkdown, .stTextInput label {
        color: #003366 !important;
        font-weight: 600;
    }

    /* Section divider line */
    hr {
        border: 1px solid #0078ff;
    }

    /* Success and error box text colors */
    .stSuccess {
        color: #004d00 !important;
    }
    .stError {
        color: #660000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============ HEADER ============
st.title("💉 Diabetes Diagnosis App")
st.subheader("An AI-Powered Tool for Early Detection")
st.markdown("---")

# ============ INPUT SECTION ============
st.header("📋 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
    Glucose = st.number_input("Glucose", min_value=0, max_value=300, step=1)
    BloodPressure = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=200, step=1)
    SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, step=1)

with col2:
    Insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=900, step=1)
    BMI = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, step=0.1)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
    Age = st.number_input("Age", min_value=1, max_value=120, step=1)

st.markdown("---")

# ============ MODEL PREDICTION ============
if st.button("🔍 Predict Diabetes"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The person is likely **Diabetic**.")
    else:
        st.success("✅ The person is likely **Non-Diabetic**.")

# ============ FOOTER ============
st.markdown("""
---
Made with ❤️ by **Om Prakash**
""")
