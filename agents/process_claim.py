import json
import os

from agents.image_analyzer import analyze_image


def clean_json(text):

    if text is None:
        return {
            "issue_type": "unknown",
            "object_part": "unknown",
            "severity": "unknown",
            "claim_status": "not_enough_information",
            "valid_image": "False"
        }

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:
        return {
            "issue_type": "unknown",
            "object_part": "unknown",
            "severity": "unknown",
            "claim_status": "not_enough_information",
            "valid_image": "False"
        }


def process_claim(row):

    claim_text = row["user_claim"]

    image_paths = row["image_paths"].split(";")

    results = []

    for image_path in image_paths:

        try:

            result_text = analyze_image(
                image_path,
                claim_text
            )

            result = clean_json(result_text)

            # Clean image id extraction
            result["image_id"] = os.path.splitext(
                os.path.basename(image_path)
            )[0]

            results.append(result)

        except Exception as e:

            print(f"\nERROR processing {image_path}")
            print(e)

            results.append({
                "issue_type": "unknown",
                "object_part": "unknown",
                "severity": "unknown",
                "claim_status": "not_enough_information",
                "valid_image": "False",
                "image_id": os.path.splitext(
                    os.path.basename(image_path)
                )[0]
            })

    return results