import google.generativeai as genai

genai.configure(api_key="AIzaSyABf_kuoOyczhnvPVypIvxfcWuh5fRVnCc")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
