def severity_score(severity):

    scores = {
        "high": 3,
        "medium": 2,
        "low": 1,
        "none": 0,
        "unknown": 0
    }

    return scores.get(severity, 0)


def combine_results(results):

    supported = []
    contradicted = []
    unclear = []

    for r in results:

        status = r.get("claim_status", "")

        if status == "supported":
            supported.append(r)

        elif status == "contradicted":
            contradicted.append(r)

        else:
            unclear.append(r)

    # Prefer supported evidence
    if supported:

        best = max(
            supported,
            key=lambda x: severity_score(
                x.get("severity", "unknown")
            )
        )

        return {
            "issue_type": best.get("issue_type", "unknown"),
            "object_part": best.get("object_part", "unknown"),
            "severity": best.get("severity", "unknown"),
            "claim_status": "supported",
            "supporting_image_ids": best.get(
                "image_id",
                "none"
            )
        }

    # If no support, return unclear
    if unclear:

        best = unclear[0]

        return {
            "issue_type": best.get("issue_type", "unknown"),
            "object_part": best.get("object_part", "unknown"),
            "severity": best.get("severity", "unknown"),
            "claim_status": "not_enough_information",
            "supporting_image_ids": "none"
        }

    # Otherwise contradicted
    if contradicted:

        best = contradicted[0]

        return {
            "issue_type": best.get("issue_type", "unknown"),
            "object_part": best.get("object_part", "unknown"),
            "severity": best.get("severity", "unknown"),
            "claim_status": "contradicted",
            "supporting_image_ids": "none"
        }

    # Safety fallback
    return {
        "issue_type": "unknown",
        "object_part": "unknown",
        "severity": "unknown",
        "claim_status": "not_enough_information",
        "supporting_image_ids": "none"
    }