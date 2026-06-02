from dotenv import load_dotenv
import os

load_dotenv("env.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "gemini-3.1-flash-lite"

MAX_STEPS = 20
MAX_SEARCH_RESULTS = 5