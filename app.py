import streamlit as st
import requests

st.title("🐧 Zoologist front")

st.write("Enter the characteristics of a penguin to predict its species.")

# User inputs
island = st.selectbox(
    "Island", ["Biscoe", "Dream", "Torgersen"]
)

bill_length_mm = st.number_input(
    "Bill length (mm)", value=51.9
)

bill_depth_mm = st.number_input(
    "Bill depth (mm)", value=19.5
)

flipper_length_mm = st.number_input(
    "Flipper length (mm)", value=206.0
)

body_mass_g = st.number_input(
    "Body mass (g)", value=3950.0
)

sex = st.selectbox("Sex", ["Male", "Female"])

# API URL
url = f"{st.secrets['API_URL']}/predict"

# API parameters
params = {
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex
}

# API request
if st.button("Predict"):
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        prediction = response.json()["prediction"]

        st.success(f"Predicted species: {prediction}")

    except requests.exceptions.RequestException as e:
        st.error(f"API error: {e}")
