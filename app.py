import streamlit as st
import pickle
import numpy as np

# Load model
with open("diabetes_model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

# Page config
st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Title styling */
    h1 {
        color: white !important;
        font-weight: 800 !important;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -1px;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.95);
        font-size: 1.3rem;
        font-weight: 300;
        margin-bottom: 3rem;
        letter-spacing: 0.5px;
    }
    
    /* Card containers */
    .card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 70px rgba(0,0,0,0.4);
    }
    
    /* Section headers */
    .section-header {
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
        border: 2px solid transparent !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        color: #2d3748 !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border: 2px solid #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        background: white !important;
    }
    
    /* Label styling */
    .stNumberInput > label {
        color: #2d3748 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 1rem 3rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        margin-top: 2rem !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Result cards */
    .result-card {
        padding: 2rem;
        border-radius: 20px;
        margin-top: 2rem;
        text-align: center;
        animation: slideIn 0.5s ease;
    }
    
    .high-risk {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        box-shadow: 0 15px 40px rgba(245, 87, 108, 0.4);
    }
    
    .low-risk {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        box-shadow: 0 15px 40px rgba(79, 172, 254, 0.4);
    }
    
    .result-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .result-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .result-message {
        font-size: 1.2rem;
        font-weight: 400;
        opacity: 0.95;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Info badge */
    .info-badge {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        color: #8b4513;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        display: inline-block;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 15px rgba(252, 182, 159, 0.3);
    }
    
    /* Grid layout */
    .input-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        margin-bottom: 1rem;
    }
    
    @media (max-width: 768px) {
        .input-grid {
            grid-template-columns: 1fr;
        }
        
        h1 {
            font-size: 2.5rem !important;
        }
        
        .card {
            padding: 1.5rem;
        }
    }
    
    /* Column styling */
    [data-testid="column"] {
        padding: 0.5rem;
    }
    
    /* Success/Error message override */
    .stAlert {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🩺 AI Diabetes Prediction</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Machine Learning for Health & Bioinformatics</div>", unsafe_allow_html=True)
st.markdown("<center><div class='info-badge'>🔬 Powered by Logistic Regression ML Model</div></center>", unsafe_allow_html=True)

# Main content in card
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>📋 Patient Health Information</div>", unsafe_allow_html=True)
st.markdown("<p style='color: #4a5568; margin-bottom: 2rem; font-size: 1rem;'>Enter the patient's medical parameters below for AI-powered diabetes risk assessment</p>", unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("👶 Pregnancies", min_value=0, max_value=20, value=0, help="Number of times pregnant")
    glucose = st.number_input("🍬 Glucose Level (mg/dL)", min_value=0, max_value=300, value=120, help="Plasma glucose concentration")
    bp = st.number_input("❤️ Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70, help="Diastolic blood pressure")
    skin = st.number_input("📏 Skin Thickness (mm)", min_value=0, max_value=100, value=20, help="Triceps skin fold thickness")

with col2:
    insulin = st.number_input("💉 Insulin Level (μU/mL)", min_value=0, max_value=900, value=80, help="2-Hour serum insulin")
    bmi = st.number_input("⚖️ BMI (kg/m²)", min_value=0.0, max_value=70.0, value=25.0, step=0.1, help="Body Mass Index")
    dpf = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01, help="Genetic diabetes likelihood")
    age = st.number_input("🎂 Age (years)", min_value=1, max_value=120, value=30, help="Patient's age")

# Predict button
if st.button("🔍 Analyze Diabetes Risk"):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0]
    
    if prediction == 1:
        risk_percentage = probability[1] * 100
        st.markdown(f"""
        <div class='result-card high-risk'>
            <div class='result-icon'>⚠️</div>
            <div class='result-title'>High Risk Detected</div>
            <div class='result-message'>Patient is likely to have diabetes</div>
            <div style='margin-top: 1.5rem; font-size: 1.1rem;'>
                Risk Probability: <strong>{risk_percentage:.1f}%</strong>
            </div>
            <div style='margin-top: 1rem; font-size: 0.95rem; opacity: 0.9;'>
                ⚕️ Recommendation: Consult with a healthcare professional immediately
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        risk_percentage = probability[0] * 100
        st.markdown(f"""
        <div class='result-card low-risk'>
            <div class='result-icon'>✅</div>
            <div class='result-title'>Low Risk Detected</div>
            <div class='result-message'>Patient is unlikely to have diabetes</div>
            <div style='margin-top: 1.5rem; font-size: 1.1rem;'>
                Healthy Probability: <strong>{risk_percentage:.1f}%</strong>
            </div>
            <div style='margin-top: 1rem; font-size: 0.95rem; opacity: 0.9;'>
                💚 Recommendation: Maintain healthy lifestyle and regular check-ups
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer info card
st.markdown("""
<div class='card' style='margin-top: 2rem; background: rgba(255,255,255,0.9);'>
    <div style='text-align: center; color: #4a5568;'>
        <h3 style='color: #667eea; margin-bottom: 1rem;'>📊 About This System</h3>
        <p style='line-height: 1.8; font-size: 0.95rem;'>
            This AI-powered system uses a <strong>Logistic Regression</strong> machine learning model trained on the 
            <strong>PIMA Indians Diabetes Dataset</strong> containing 768 patient records. The model analyzes 8 key 
            health parameters to predict diabetes risk with high accuracy. This tool is designed to assist healthcare 
            professionals in early diabetes detection and risk assessment.
        </p>
        <p style='margin-top: 1rem; font-size: 0.85rem; color: #718096;'>
            ⚠️ <em>Disclaimer: This is a predictive tool and should not replace professional medical diagnosis.</em>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
