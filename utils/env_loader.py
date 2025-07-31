from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
AI_MODEL = "google/gemini-2.5-flash"