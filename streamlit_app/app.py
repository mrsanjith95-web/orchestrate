
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import pandas as pd

from agents.process_claim import process_claim
from agents.multi_image_decision import combine_results

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Insurance Claim Verification",
    page_icon="🔍",
    layout="wide"
)

# -------------------------
# Title
# -------------------------

st.title("🔍 Insurance Claim Verification System")

st.markdown(
    "Upload damage images and enter the customer claim for AI-based verification."
)

# -------------------------
# Claim Input
# -------------------------

claim_text = st.text_area(
    "Enter Claim",
    height=120,
    placeholder="Customer: My laptop screen is cracked..."
)

# -------------------------
# Image Upload
# -------------------------

uploaded_files = st.file_uploader(
    "Upload Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# -------------------------
# Image Preview
# -------------------------

if uploaded_files:

    st.subheader("📷 Uploaded Images")

    cols = st.columns(min(3, len(uploaded_files)))

    for i, file in enumerate(uploaded_files):

        with cols[i % len(cols)]:

            st.image(
                file,
                caption=file.name,
                width=200
            )

# -------------------------
# Verify Button
# -------------------------

if st.button("🔎 Verify Claim"):

    if not claim_text:
        st.error("Please enter claim text.")
        st.stop()

    if not uploaded_files:
        st.error("Please upload images.")
        st.stop()

    # -------------------------
    # Create Upload Folder
    # -------------------------

    UPLOAD_DIR = os.path.join(
        os.path.dirname(__file__),
        "uploads"
    )

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    saved_paths = []

    # -------------------------
    # Save Uploaded Images
    # -------------------------

    for file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_DIR,
            file.name
        )

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        saved_paths.append(save_path)

    # -------------------------
    # Create Fake Dataset Row
    # -------------------------

    fake_row = pd.Series({
        "user_claim": claim_text,
        "image_paths": ";".join(saved_paths)
    })

    # -------------------------
    # Run AI Analysis
    # -------------------------

    with st.spinner("🤖 AI is analyzing images..."):

        image_results = process_claim(fake_row)

        final = combine_results(image_results)

    # -------------------------
    # Results
    # -------------------------

    st.success("✅ Analysis Complete")

    st.markdown("---")
    st.header("📋 Analysis Result")

    st.write(
        "**Issue Type:**",
        final.get("issue_type", "unknown")
    )

    st.write(
        "**Object Part:**",
        final.get("object_part", "unknown")
    )

    # -------------------------
    # Claim Status
    # -------------------------

    status = final.get(
        "claim_status",
        "not_enough_information"
    )

    if status == "supported":
        st.success(f"Claim Status: {status}")

    elif status == "contradicted":
        st.error(f"Claim Status: {status}")

    else:
        st.warning(f"Claim Status: {status}")

    # -------------------------
    # Severity
    # -------------------------

    severity = final.get(
        "severity",
        "unknown"
    )

    if severity == "high":
        st.error(f"Severity: {severity}")

    elif severity == "medium":
        st.warning(f"Severity: {severity}")

    else:
        st.info(f"Severity: {severity}")

    # -------------------------
    # Supporting Images
    # -------------------------

    supporting = final.get(
        "supporting_image_ids",
        "none"
    )

    st.write(
        "**Supporting Images:**",
        supporting
    )
