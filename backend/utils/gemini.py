import markdown
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load your Gemini API key from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# ✅ Common helper function to convert Markdown to HTML
def convert_markdown_to_html(markdown_text: str) -> str:
    return markdown.markdown(markdown_text.strip())

# ✅ Chatbot-style Gemini response
async def generate_gemini_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        html_output = convert_markdown_to_html(response.text)
        return html_output
    except Exception as e:
        print("Gemini error:", e)
        return "<p>❌ Sorry, I couldn't process your question right now.</p>"

# ✅ Soil Recommendation function
def get_soil_recommendations(soil_data: dict, fertility_result: str) -> str:
    prompt = f"""
    Soil Test Result: {fertility_result}
    Parameters:
    {soil_data}

    Based on the soil data and the result, give expert-level suggestions to improve fertility. Be clear and concise. Use simple language a farmer can understand. Highlight important words using bold. Keep the suggestions short.
    """
    try:
        response = model.generate_content(prompt)
        html_output = convert_markdown_to_html(response.text)
        return html_output
    except Exception as e:
        print("Gemini recommendation error:", e)
        return "<p>❌ Couldn't generate soil recommendations.</p>"
