import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AAIzaSyBs4TVsOU0BQzKDg07Unm9Ir5Gmxt__OQM")

models = genai.list_models()
for model in models:
    print(model.name)
