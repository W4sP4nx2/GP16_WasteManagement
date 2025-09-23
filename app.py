import streamlit as st
from PIL import Image
import numpy as np

st.title("♻️ Waste Classifier & Recycling Advisor")

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # For now: dummy prediction
    predicted_class = "plastic"
    advice_dict = {
        "plastic": "Rinse and place in plastics recycling bin.",
        "paper": "Keep dry. Recycle with paper products.",
        "glass": "Rinse and recycle separately.",
        "metal": "Check if accepted in local recycling.",
        "organic": "Compost if possible.",
        "other": "Dispose properly according to local rules."
    }

    st.subheader(f"Prediction: {predicted_class}")
    st.info(f"Recycling advice: {advice_dict[predicted_class]}")
