import streamlit as st
import google.generativeai as genai
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure Gemini API with placeholder key
genai.configure(api_key="AIzaSyABf_kuoOyczhnvPVypIvxfcWuh5fRVnCc")

# Streamlit UI
st.title("🌱 Smart Farming Assistant")
st.write("Get region-specific, multilingual farming advice powered by Gemini 1.5")

# User inputs
location = st.text_input("Enter your location (e.g., Tamil Nadu, India)")
crop_stage = st.selectbox("Select crop stage", ["Planting", "Growing", "Harvesting"])
constraints = st.text_input("Constraints (e.g., organic-only, low water availability)")
query = st.text_area("Ask your farming question")

# Generate response
if st.button("Get Advice"):
    if query.strip() == "":
        st.warning("Please enter a farming question.")
    else:
        prompt = f"Location: {location}\nCrop Stage: {crop_stage}\nConstraints: {constraints}\nQuestion: {query}"
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        # Display AI response
        st.subheader("AI Farming Advice")
        st.write(response.text)

        # Example: visualize dummy rainfall data (just to show matplotlib/seaborn usage)
        st.subheader("📊 Example Visualization")
        rainfall_data = pd.DataFrame({
            "Month": ["June", "July", "August", "September"],
            "Rainfall (mm)": [120, 200, 180, 90]
        })
        fig, ax = plt.subplots()
        sns.barplot(x="Month", y="Rainfall (mm)", data=rainfall_data, ax=ax)
        st.pyplot(fig)
