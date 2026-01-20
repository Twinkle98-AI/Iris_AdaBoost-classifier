import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(
    page_title="AdaBoost Iris Classifier",
    page_icon="🌸",
    layout="centered"
)

# Load model
model = pickle.load(open("adaboost_model.pkl", "rb"))

# Title
st.markdown("<h1 style='text-align:center;'>🌸 AdaBoost Iris Classification</h1>", unsafe_allow_html=True)
st.write("Predict Iris flower species using an AdaBoost ensemble model.")

st.divider()

# Sidebar inputs
st.sidebar.header("🔢 Input Features")

sepal_length = st.sidebar.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width  = st.sidebar.number_input("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.number_input("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width  = st.sidebar.number_input("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction
if st.sidebar.button("Predict 🌼"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]

    species_map = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    st.subheader("🔍 Prediction Result")
    st.success(f"Predicted Iris Species: **{species_map[prediction]}**")

st.divider()
st.caption("Built using AdaBoost | Scikit-learn | Streamlit")

