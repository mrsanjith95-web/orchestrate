from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What is AI?"
    )
    print("SUCCESS")
    print(response.text[:200])

except Exception as e:
    print("FAILED")
    print(e)