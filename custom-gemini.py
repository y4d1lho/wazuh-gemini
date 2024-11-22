import google.generativeai as genai
import os

genai.configure(api_key=os.environ["AIzaSyB0644J9EYPW1mvpO4UcacjXuST_YtvSbs"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
