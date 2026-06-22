from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_claim(claim_text):

    prompt = f"""
You are an insurance claim analyzer.

Claim:
{claim_text}

Extract ONLY the following information:

1. object_type (car/laptop/package)
2. damage_type
3. damaged_part

Rules:
- Focus on the DAMAGE, not the cause.
- Example:
  "Laptop screen cracked after falling"
  damage_type = "crack"
  damaged_part = "screen"

Return ONLY valid JSON.

Example:

{{
    "object_type": "laptop",
    "damage_type": "crack",
    "damaged_part": "screen"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text