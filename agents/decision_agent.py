def decide(image_result):

    status = image_result.get(
        "claim_supported",
        ""
    ).lower()

    if status == "yes":
        return "supported"

    elif status == "no":
        return "contradicted"

    else:
        return "not_enough_information"