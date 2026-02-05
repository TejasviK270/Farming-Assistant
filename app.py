import streamlit as st
import google.generativeai as genai

# Configure Gemini API with your real key
genai.configure(api_key="AIzaSyC5Rt-y-UZxT_XU3ffuew1M5Ni340wu9kE")

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

        # Add instruction for concise bullet points
        prompt = (
            f"Location: {location}\n"
            f"Crop Stage: {crop_stage}\n"
            f"Constraints: {constraints}\n"
            f"Question: {query}\n\n"
            "Please answer in 3-5 short bullet points, simple language for farmers."
        )

        response = model.generate_content(contents=prompt)

        st.subheader("🌾 AI Farming Advice (Bullet Points)")
        # Split response into lines and show as bullets
        for line in response.text.split("\n"):
            line = line.strip()
            if line:
                st.markdown(f"- {line}")
    else:
        st.warning("Please enter a farming question.")
