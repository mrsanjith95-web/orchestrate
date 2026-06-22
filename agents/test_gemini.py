from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MAX_RETRIES = 5

for attempt in range(MAX_RETRIES):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="What is AI?"
        )

        print(response.text)
        break

    except Exception as e:

        error_text = str(e)

        print(f"Attempt {attempt+1} failed")

        if "429" in error_text:

            wait_time = min(60 * (attempt + 1), 300)

            print(f"Quota exceeded. Waiting {wait_time} seconds...")
            time.sleep(wait_time)

        else:

            print("Non-quota error:")
            print(error_text)
            break

else:
    print("All retries failed.")