"""
app.py
-------
The web app for the Disease Prediction project. Combines:
  - A general Symptom Checker (41 diseases, from symptoms)
  - 3 specialist checkers: Diabetes, Heart Disease, Breast Cancer

Run with:  streamlit run app.py
(Run this command from INSIDE the "app" folder, so the "../models" paths
 below correctly point to the trained models saved by the notebooks.)
"""

import json
import os

import joblib
import numpy as np
import pandas as pd
import streamlit as st

from disease_info import DISEASE_INFO, SPECIALIST_INFO

MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

st.set_page_config(
    page_title="PrevenTx: Multi-Disease Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Styling — a bit of custom CSS so this looks like a real product, not a
# default Streamlit demo. Colors are intentionally calm/clinical (teal,
# white, soft red/green for results) rather than flashy.
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(135deg, #0f766e 0%, #115e59 100%);
        padding: 2rem 2rem 1.5rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { margin: 0; font-size: 2.1rem; }
    .main-header p { margin: 0.4rem 0 0 0; opacity: 0.9; font-size: 1.0rem; }

    .checker-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        height: 100%;
    }
    .checker-card h3 { margin-top: 0; color: #0f766e; }
    .checker-card .acc { font-size: 0.85rem; color: #64748b; }

    .result-positive {
        background: #fef2f2;
        border-left: 6px solid #dc2626;
        padding: 1.1rem 1.4rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .result-negative {
        background: #f0fdf4;
        border-left: 6px solid #16a34a;
        padding: 1.1rem 1.4rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .result-positive h2, .result-negative h2 { margin: 0 0 0.3rem 0; }

    .disclaimer {
        background: #fffbeb;
        border: 1px solid #fde68a;
        border-radius: 10px;
        padding: 0.8rem 1.1rem;
        font-size: 0.85rem;
        color: #92400e;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------------------------------
# Cached loaders — st.cache_resource means these files are only read from
# disk ONCE, the first time they're needed, no matter how many times the
# user interacts with the app afterward. Big speed win.
# --------------------------------------------------------------------------
@st.cache_resource
def load_specialist(prefix: str):
    model = joblib.load(os.path.join(MODELS_DIR, f"{prefix}_model.joblib"))
    scaler = joblib.load(os.path.join(MODELS_DIR, f"{prefix}_scaler.joblib"))
    with open(os.path.join(MODELS_DIR, f"{prefix}_metadata.json")) as f:
        metadata = json.load(f)
    return model, scaler, metadata


@st.cache_resource
def load_symptom_model():
    model = joblib.load(os.path.join(MODELS_DIR, "symptom_model.joblib"))
    label_encoder = joblib.load(os.path.join(MODELS_DIR, "symptom_label_encoder.joblib"))
    with open(os.path.join(MODELS_DIR, "symptom_metadata.json")) as f:
        metadata = json.load(f)
    return model, label_encoder, metadata


def disclaimer():
    st.markdown(
        '<div class="disclaimer">⚠️ <b>Disclaimer:</b> This tool is an educational/portfolio '
        "project and is <b>not</b> a certified medical device. Predictions are based on limited "
        "training data and should never replace professional medical advice, diagnosis, or treatment. "
        "Always consult a qualified doctor.</div>",
        unsafe_allow_html=True,
    )


# --------------------------------------------------------------------------
# Field definitions for the 3 specialist forms.
# Each entry: (label, kind, options/range, default, help text)
#   kind == "slider"    -> options = (min, max, step)
#   kind == "select"    -> options = {display_label: actual_value}
# These ranges come directly from the training data, so every default is a
# realistic, typical value (the median from the dataset).
# --------------------------------------------------------------------------
DIABETES_FIELDS = [
    ("Pregnancies", "slider", (0, 17, 1), 1, "Number of times pregnant"),
    ("Glucose", "slider", (44, 199, 1), 117, "Plasma glucose concentration (mg/dL)"),
    ("BloodPressure", "slider", (24, 122, 1), 72, "Diastolic blood pressure (mm Hg)"),
    ("SkinThickness", "slider", (7, 99, 1), 23, "Triceps skin fold thickness (mm)"),
    ("Insulin", "slider", (14, 846, 1), 30, "2-Hour serum insulin (mu U/mL)"),
    ("BMI", "slider", (18.0, 67.0, 0.1), 25.0, "Body Mass Index"),
    ("DiabetesPedigreeFunction", "slider", (0.05, 2.50, 0.01), 0.37, "Genetic diabetes risk score"),
    ("Age", "slider", (21, 81, 1), 29, "Age in years"),
]

HEART_FIELDS = [
    ("age", "slider", (29, 77, 1), 50, "Age in years"),
    ("sex", "select", {"Male": 1, "Female": 0}, "Male", "Biological sex"),
    ("cp", "select", {"Typical angina": 1, "Atypical angina": 2, "Non-anginal pain": 3, "Asymptomatic": 4}, "Typical angina", "Chest pain type"),
    ("trestbps", "slider", (94, 200, 1), 120, "Resting blood pressure (mm Hg)"),
    ("chol", "slider", (126, 564, 1), 200, "Serum cholesterol (mg/dL)"),
    ("fbs", "select", {"No": 0, "Yes": 1}, "No", "Fasting blood sugar > 120 mg/dL?"),
    ("restecg", "select", {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}, "Normal", "Resting ECG result"),
    ("thalach", "slider", (71, 202, 1), 150, "Maximum heart rate achieved"),
    ("exang", "select", {"No": 0, "Yes": 1}, "No", "Exercise-induced angina?"),
    ("oldpeak", "slider", (0.0, 6.2, 0.1), 0.8, "ST depression induced by exercise"),
    ("slope", "select", {"Upsloping": 1, "Flat": 2, "Downsloping": 3}, "Flat", "Slope of peak exercise ST segment"),
    ("ca", "select", {"0": 0, "1": 1, "2": 2, "3": 3}, "0", "Number of major vessels colored by fluoroscopy"),
    ("thal", "select", {"Normal": 3, "Fixed defect": 6, "Reversible defect": 7}, "Normal", "Thalassemia test result"),
]

BREAST_CANCER_FIELDS = [
    ("mean radius", "slider", (6.9, 28.2, 0.1), 14.0, "Mean distance from center to perimeter points"),
    ("mean texture", "slider", (9.7, 39.3, 0.1), 19.0, "Standard deviation of gray-scale values"),
    ("mean perimeter", "slider", (43.0, 189.0, 1.0), 90.0, "Mean perimeter of the cell nuclei"),
    ("mean area", "slider", (143.0, 2502.0, 1.0), 550.0, "Mean area of the cell nuclei"),
    ("mean smoothness", "slider", (0.05, 0.17, 0.001), 0.096, "Mean local variation in radius lengths"),
    ("mean compactness", "slider", (0.02, 0.35, 0.001), 0.093, "Mean of (perimeter^2 / area - 1.0)"),
    ("mean concavity", "slider", (0.0, 0.43, 0.001), 0.06, "Mean severity of concave portions of the contour"),
    ("mean concave points", "slider", (0.0, 0.21, 0.001), 0.03, "Mean number of concave portions of the contour"),
    ("mean symmetry", "slider", (0.10, 0.31, 0.001), 0.18, "Mean symmetry of the cell nuclei"),
    ("mean fractal dimension", "slider", (0.05, 0.10, 0.0005), 0.063, "Mean 'coastline approximation' of the nuclei"),
]


def render_specialist_form(disease_key: str, prefix: str, fields: list):
    """Shared rendering logic for the 3 specialist checkers (Diabetes,
    Heart Disease, Breast Cancer). One function handles all three, since
    they all follow the exact same pattern: show a form, collect inputs in
    the right order, scale them, and run the saved model.
    """
    model, scaler, metadata = load_specialist(prefix)

    st.markdown(f"## {disease_key} Checker")
    st.caption(SPECIALIST_INFO.get(disease_key, ""))
    m = metadata["metrics"]
    st.caption(
        f"Model used: **{metadata['best_model']}** · "
        f"Accuracy: **{m['Accuracy']*100:.1f}%** · "
        f"ROC-AUC: **{m['ROC-AUC']:.3f}**"
    )

    with st.form(key=f"{prefix}_form"):
        cols = st.columns(2)
        values = {}
        for i, (name, kind, opts, default, help_text) in enumerate(fields):
            col = cols[i % 2]
            with col:
                if kind == "slider":
                    lo, hi, step = opts
                    values[name] = st.slider(name, min_value=lo, max_value=hi, value=default, step=step, help=help_text)
                else:  # select
                    label_to_val = opts
                    chosen_label = st.selectbox(name, options=list(label_to_val.keys()), index=list(label_to_val.keys()).index(default), help=help_text)
                    values[name] = label_to_val[chosen_label]
        submitted = st.form_submit_button("🔍 Predict", use_container_width=True, type="primary")

    if submitted:
        feature_order = metadata["feature_names"]
        X = pd.DataFrame([[values[f] for f in feature_order]], columns=feature_order)
        X_scaled = scaler.transform(X)
        pred = model.predict(X_scaled)[0]
        proba = model.predict_proba(X_scaled)[0]
        confidence = proba[pred] * 100
        class_names = metadata["class_names"]

        if pred == 1:
            st.markdown(
                f'<div class="result-positive"><h2>⚠️ {class_names[1]}</h2>'
                f"Model confidence: <b>{confidence:.1f}%</b></div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="result-negative"><h2>✅ {class_names[0]}</h2>'
                f"Model confidence: <b>{confidence:.1f}%</b></div>",
                unsafe_allow_html=True,
            )
        disclaimer()


def render_home():
    st.markdown(
        """
        <div class="main-header">
            <h1>🩺 PrevenTx: Multi-Disease Prediction System</h1>
            <p>A machine learning powered tool combining a general symptom checker
            with 3 specialist diagnostic models — built end-to-end as a learning project.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = [
        ("🤒", "Symptom Checker", "Pick your symptoms, get the most likely disease out of 41 possibilities.", "symptom_metadata.json"),
        ("🩸", "Diabetes Checker", "Enter clinical values (glucose, BMI, etc.) for a focused diabetes risk check.", "diabetes_metadata.json"),
        ("❤️", "Heart Disease Checker", "Enter cardiac measurements for a focused heart disease risk check.", "heart_metadata.json"),
        ("🔬", "Breast Cancer Checker", "Enter cell-measurement values for a focused tumor classification.", "breast_cancer_metadata.json"),
    ]
    cols = st.columns(4)
    for col, (icon, title, desc, meta_file) in zip(cols, cards):
        with open(os.path.join(MODELS_DIR, meta_file)) as f:
            meta = json.load(f)
        acc = meta.get("accuracy", meta.get("metrics", {}).get("Accuracy"))
        with col:
            st.markdown(
                f"""
                <div class="checker-card">
                    <h3>{icon} {title}</h3>
                    <p>{desc}</p>
                    <p class="acc">Model: {meta['best_model']} &middot; Accuracy: {acc*100:.1f}%</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.info("👈 Use the sidebar to pick a checker and get started.")
    disclaimer()


def render_symptom_checker():
    model, label_encoder, metadata = load_symptom_model()
    feature_names = metadata["feature_names"]
    pretty_names = {f: f.replace("_", " ").title() for f in feature_names}
    pretty_to_raw = {v: k for k, v in pretty_names.items()}

    st.markdown("## 🤒 General Symptom Checker")
    st.caption(
        f"Model used: **{metadata['best_model']}** · Trained on 41 diseases · "
        f"Test accuracy: **{metadata['accuracy']*100:.0f}%** "
        "(see the notebook for why this number is so high — the underlying dataset is very repetitive)."
    )

    selected_pretty = st.multiselect(
        "Type to search and select your symptoms:",
        options=sorted(pretty_to_raw.keys()),
        help="Select as many symptoms as apply. The more you select, the more confident the prediction.",
    )

    predict_clicked = st.button("🔍 Predict Disease", type="primary", use_container_width=True)

    if predict_clicked:
        if not selected_pretty:
            st.warning("Please select at least one symptom.")
            return

        input_vector = pd.DataFrame(0, index=[0], columns=feature_names)
        for p in selected_pretty:
            input_vector.loc[0, pretty_to_raw[p]] = 1

        proba = model.predict_proba(input_vector)[0]
        top3_idx = np.argsort(proba)[::-1][:3]

        st.markdown("### Top 3 most likely diseases")
        for rank, idx in enumerate(top3_idx, start=1):
            disease_name = label_encoder.inverse_transform([idx])[0]
            confidence = proba[idx] * 100
            st.markdown(f"**{rank}. {disease_name}** — {confidence:.1f}% confidence")
            st.progress(min(confidence / 100, 1.0))

        top_disease = label_encoder.inverse_transform([top3_idx[0]])[0]
        info = DISEASE_INFO.get(top_disease)
        if info:
            st.markdown(f"#### About {top_disease}")
            st.write(info["description"])
            st.markdown("**General precautions:**")
            for p in info["precautions"]:
                st.markdown(f"- {p}")
        disclaimer()


# --------------------------------------------------------------------------
# Sidebar navigation
# --------------------------------------------------------------------------
st.sidebar.title("🩺 Navigation")
page = st.sidebar.radio(
    "Choose a checker:",
    ["🏠 Home", "🤒 Symptom Checker", "🩸 Diabetes", "❤️ Heart Disease", "🔬 Breast Cancer"],
)
st.sidebar.markdown("---")
st.sidebar.caption("Disease Prediction using Machine Learning — student project by Payal")

if page == "🏠 Home":
    render_home()
elif page == "🤒 Symptom Checker":
    render_symptom_checker()
elif page == "🩸 Diabetes":
    render_specialist_form("Diabetes", "diabetes", DIABETES_FIELDS)
elif page == "❤️ Heart Disease":
    render_specialist_form("Heart Disease", "heart", HEART_FIELDS)
elif page == "🔬 Breast Cancer":
    render_specialist_form("Breast Cancer", "breast_cancer", BREAST_CANCER_FIELDS)
