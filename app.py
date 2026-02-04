import streamlit as st
import google.generativeai as genai

# Configure Gemini API with your real key
genai.configure(api_key="AIzaSyDHvsFSKhv8gs8W0pER1ujeW2Uoe1fqP_s")

st.title("🌱 Smart Farming Assistant")
st.write("Get region-specific, multilingual farming advice powered by Gemini")

# User inputs
location = st.text_input("Enter your location (e.g., Tamil Nadu, India)")
crop_stage = st.selectbox("Select crop stage", ["Planting", "Growing", "Harvesting"])
constraints = st.text_input("Constraints (e.g., organic-only, low water availability)")
query = st.text_area("Ask your farming question")

if st.button("Get Advice"):
    if query.strip():
        # ✅ Use a supported model
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        prompt = f"Location: {location}\nCrop Stage: {crop_stage}\nConstraints: {constraints}\nQuestion: {query}"
        response = model.generate_content(prompt)

        st.subheader("AI Farming Advice")
        st.write(response.text)
    else:
        st.warning("Please enter a farming question.")
