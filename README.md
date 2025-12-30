# 🩺 AI Diabetes Prediction System

An advanced machine learning web application for predicting diabetes risk using patient health parameters. Built with **Streamlit** and **Scikit-learn**, featuring a modern, visually stunning UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![ML](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Try it Live!

**🌐 Live Demo:** [https://magudeshwaran-diabetes-prediction.streamlit.app/](https://magudeshwaran-diabetes-prediction.streamlit.app/)

Experience the AI-powered diabetes prediction system in action! No installation required - just click the link above to start analyzing diabetes risk instantly.

---

## 🌟 Features

- ✨ **Beautiful Modern UI** - Stunning gradient design with glassmorphism effects
- 🤖 **AI-Powered Predictions** - Logistic Regression model trained on real medical data
- 📊 **Probability Display** - Shows exact risk percentage for transparency
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- 🎯 **User-Friendly Interface** - Intuitive input fields with helpful tooltips
- ⚡ **Real-Time Results** - Instant predictions with animated result cards
- 🔬 **Medical-Grade Accuracy** - Trained on PIMA Indians Diabetes Dataset

## 📂 Project Structure

```
diabetes_prediction/
│
├── app.py                    # Streamlit web application
├── model.py                  # ML model training script
├── diabetes.csv              # Dataset (768 patient records)
├── diabetes_model.pkl        # Trained model & scaler
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 📊 Dataset Information

### PIMA Indians Diabetes Dataset

**Source:** [Machine Learning Repository - Jason Brownlee](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv)

**Original Dataset:** The PIMA Indians Diabetes Dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict whether a patient has diabetes based on diagnostic measurements.

**Dataset Details:**
- **Total Records:** 768 patient records
- **Features:** 8 medical predictor variables
- **Target:** Binary classification (0 = No Diabetes, 1 = Diabetes)

### Features (Columns)

| Feature | Description | Unit |
|---------|-------------|------|
| **Pregnancies** | Number of times pregnant | Count |
| **Glucose** | Plasma glucose concentration (2 hours in oral glucose tolerance test) | mg/dL |
| **BloodPressure** | Diastolic blood pressure | mm Hg |
| **SkinThickness** | Triceps skin fold thickness | mm |
| **Insulin** | 2-Hour serum insulin | μU/mL |
| **BMI** | Body Mass Index | kg/m² |
| **DiabetesPedigreeFunction** | Diabetes pedigree function (genetic likelihood) | Float |
| **Age** | Age of the patient | Years |
| **Outcome** | Class variable (0 or 1) | Binary |

### Dataset Download

The dataset was automatically downloaded from:
```
https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv
```

**Citation:**
- Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download the Project

```bash
cd diabetes_prediction
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `streamlit` - Web application framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning library

### Step 3: Train the Model

```bash
python model.py
```

**Output:**
```
Model trained and saved successfully!
```

This will:
- Load the `diabetes.csv` dataset
- Preprocess and scale the data using StandardScaler
- Train a Logistic Regression model
- Save the trained model and scaler to `diabetes_model.pkl`

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your default browser at:
```
http://localhost:8501
```

## 💻 Usage

1. **Enter Patient Information:**
   - Fill in all 8 health parameters in the input fields
   - Each field has helpful tooltips explaining what to enter

2. **Analyze Risk:**
   - Click the "🔍 ANALYZE DIABETES RISK" button
   - The AI model will process the data instantly

3. **View Results:**
   - **High Risk:** Red gradient card with risk percentage and medical recommendations
   - **Low Risk:** Blue gradient card with healthy probability and lifestyle tips

### Example Input Values

**High Risk Example:**
```
Pregnancies: 6
Glucose: 148 mg/dL
Blood Pressure: 72 mm Hg
Skin Thickness: 35 mm
Insulin: 0 μU/mL
BMI: 33.6 kg/m²
Diabetes Pedigree Function: 0.627
Age: 50 years
```

**Low Risk Example:**
```
Pregnancies: 1
Glucose: 85 mg/dL
Blood Pressure: 66 mm Hg
Skin Thickness: 29 mm
Insulin: 0 μU/mL
BMI: 26.6 kg/m²
Diabetes Pedigree Function: 0.351
Age: 31 years
```

## 🧠 Model Details

### Algorithm: Logistic Regression

**Why Logistic Regression?**
- Excellent for binary classification problems
- Provides probability estimates
- Fast training and prediction
- Interpretable results
- Works well with medical datasets

### Model Training Process

1. **Data Loading:** Read diabetes.csv dataset
2. **Feature Separation:** Separate features (X) from target (y)
3. **Scaling:** StandardScaler normalization for better performance
4. **Train-Test Split:** 80% training, 20% testing (random_state=42)
5. **Model Training:** Fit Logistic Regression on training data
6. **Model Persistence:** Save model and scaler using pickle

### Model Performance

The model is trained on 614 samples and tested on 154 samples from the PIMA Indians dataset, providing reliable predictions for diabetes risk assessment.

## 🎨 UI Features

### Design Elements

- **Gradient Background:** Purple-to-violet gradient (135deg, #667eea → #764ba2)
- **Glassmorphism Cards:** Frosted glass effect with backdrop blur
- **Custom Typography:** Inter font family for modern aesthetics
- **Smooth Animations:** Hover effects, slide-in animations, transitions
- **Responsive Layout:** Two-column grid that adapts to screen size

### Color Palette

| Element | Colors |
|---------|--------|
| Primary Background | Purple Gradient (#667eea → #764ba2) |
| High Risk Card | Pink-Red Gradient (#f093fb → #f5576c) |
| Low Risk Card | Blue-Cyan Gradient (#4facfe → #00f2fe) |
| Info Badge | Peach Gradient (#ffecd2 → #fcb69f) |
| Input Fields | Gray Gradient (#f5f7fa → #c3cfe2) |

## 🔧 Technical Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web application framework |
| **Scikit-learn** | Machine learning library |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Pickle** | Model serialization |

## 📈 Future Enhancements

- [ ] Add more ML models (Random Forest, SVM, Neural Networks)
- [ ] Model comparison dashboard
- [ ] Feature importance visualization
- [ ] Historical predictions tracking
- [ ] Export predictions to PDF
- [ ] Multi-language support
- [ ] Dark/Light theme toggle
- [ ] API endpoint for integration

## ⚠️ Disclaimer

This is a **predictive tool** designed to assist healthcare professionals in early diabetes detection and risk assessment. It should **NOT replace professional medical diagnosis** or consultation with qualified healthcare providers.

## 📄 License

This project is licensed under the MIT License - feel free to use, modify, and distribute.

## 👨‍💻 Author

Created with ❤️ for Health & Bioinformatics

## 🙏 Acknowledgments

- **PIMA Indians Diabetes Dataset** - National Institute of Diabetes and Digestive and Kidney Diseases
- **Jason Brownlee** - For hosting the dataset repository
- **Streamlit Team** - For the amazing web framework
- **Scikit-learn Community** - For the powerful ML library

---

**Made with Python 🐍 | Powered by AI 🤖 | Designed for Healthcare 🩺**
