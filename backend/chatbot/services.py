import google.generativeai as genai
from django.conf import settings


def get_gemini_response(user_message):
    """Get response from Gemini AI"""
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in settings")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    # 1. Define the system instructions (your prompt)
    system_instructions = """
    Act as a world-class Physics Expert. 
    Rules:
    - State core physical principles first.
    - Use LaTeX for equations.
    - If the question is not about physics, reply: 'I am a Physics Expert!'
    """
    
    # 2. Combine instructions with the user's actual question
    full_prompt = f"{system_instructions}\n\nUser Question: {user_message}"

    try:
        # 3. Pass the combined prompt to the model
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Error getting response from Gemini AI: {str(e)}")


