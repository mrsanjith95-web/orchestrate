from google import genai
from PIL import Image
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def fallback_response():
    return """
{
    "issue_type":"unknown",
    "object_part":"unknown",
    "severity":"unknown",
    "claim_status":"not_enough_information",
    "valid_image":"False"
}
"""


def analyze_image(image_path, claim_text):

    try:
        image = Image.open(image_path)

    except Exception as e:
        print("Image open error:", e)
        return fallback_response()

    prompt = f"""
Claim:
{claim_text}

Return ONLY valid JSON.

issue_type:
broken_part, crack, crushed_packaging, dent,
none, scratch, stain, torn_packaging,
unknown, water_damage

object_part:
contents, corner, door, front_bumper,
headlight, hinge, keyboard,
package_corner, package_side,
rear_bumper, screen, seal,
side_mirror, trackpad,
unknown, windshield

severity:
high, medium, low, none, unknown

claim_status:
supported, contradicted,
not_enough_information

JSON:

{{
"issue_type":"",
"object_part":"",
"severity":"",
"claim_status":"",
"valid_image":"True"
}}
"""

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, image]
            )

            if not response:
                return fallback_response()

            response_text = getattr(response, "text", None)

            if not response_text:
                return fallback_response()

            response_text = (
                response_text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            return response_text

        except Exception as e:

            error_text = str(e)

            print(f"\nAttempt {attempt + 1} failed:")
            print(error_text)

            if "429" in error_text:

                print("Quota or rate limit reached.")

                if attempt < MAX_RETRIES - 1:
                    time.sleep(20)
                    continue

                return fallback_response()

            elif "503" in error_text:

                print("Gemini busy.")

                if attempt < MAX_RETRIES - 1:
                    time.sleep(30)
                    continue

                return fallback_response()

            else:

                if attempt < MAX_RETRIES - 1:
                    print("Retrying in 10 seconds...")
                    time.sleep(10)
                else:
                    return fallback_response()

    return fallback_response()


if __name__ == "__main__":

    result = analyze_image(
        "images/test/case_001/img_1.jpg",
        "The front bumper and headlight are damaged."
    )

    print(result)