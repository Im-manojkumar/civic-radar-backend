import os
import logging
from google import genai
from google.genai import types

logger = logging.getLogger("civic_radar")

# Try to get API Key from env
API_KEY = os.environ.get("API_KEY") or os.environ.get("GEMINI_API_KEY")

def generate_alert_explanation(prompt_text: str) -> str | None:
    """
    Generates a text summary using Gemini.
    Returns None if API key is missing or request fails.
    """
    if not API_KEY:
        logger.warning("Gemini API Key missing. Skipping LLM generation.")
        return None

    try:
        client = genai.Client(api_key=API_KEY)
        
        # Using the model specified for basic text tasks in guidelines
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp", 
            contents=prompt_text,
            config=types.GenerateContentConfig(
                temperature=0.3, # Low temperature for factual summarization
                max_output_tokens=300
            )
        )
        return response.text
    except Exception as e:
        logger.error(f"Gemini generation failed: {e}")
        return None
