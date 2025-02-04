from django.conf import settings
import google.generativeai as genai
genai.configure(api_key=settings.OPENAI_API_KEY)

def analyze_error(error_trace):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    I ran this Python code and got the following error:
    {error_trace}

    1. Identify the issue and the probable cause.
    2. Mention the file and line number if available.
    3. Suggest a corrected version of the code.
    """
    response = model.generate_content(prompt)
    return response.text