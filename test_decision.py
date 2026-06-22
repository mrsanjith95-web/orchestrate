from agents.decision_agent import decide

image_result = {
    "object_type": "laptop",
    "visible_damage": "no",
    "damaged_part": "none",
    "severity": "none",
    "claim_supported": "no"
}

result = decide(image_result)

print("Decision:", result)