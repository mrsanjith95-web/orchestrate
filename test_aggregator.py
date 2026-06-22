from agents.multi_image_decision import combine_results

results = [
    {
        "issue_type": "none",
        "object_part": "front_bumper",
        "severity": "none",
        "claim_status": "contradicted",
        "image_id": "img_1"
    },
    {
        "issue_type": "scratch",
        "object_part": "front_bumper",
        "severity": "medium",
        "claim_status": "supported",
        "image_id": "img_2"
    },
    {
        "issue_type": "none",
        "object_part": "headlight",
        "severity": "none",
        "claim_status": "contradicted",
        "image_id": "img_3"
    }
]

final_result = combine_results(results)

print(final_result)