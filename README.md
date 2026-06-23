# Insurance Claim Verification System

An AI-powered insurance claim verification system that analyzes uploaded images and customer claim conversations to determine whether a claim is supported, contradicted, or lacks sufficient evidence.

## Features

- Image-based damage verification
- Gemini AI powered image analysis
- Multi-image evidence aggregation
- Severity assessment
- Support for:
  - Cars
  - Laptops
  - Packages
- Streamlit dashboard interface

## Tech Stack

- Python
- Google Gemini API
- Streamlit
- Pandas
- Pillow

## Project Structure

agents/
data/
images/
streamlit_app/
main.py

## Run Locally

pip install -r requirements.txt

streamlit run streamlit_app/app.py

## Example Output

Issue Type: crack
Object Part: screen
Claim Status: supported
Severity: high

## Screenshots

### Architecture
![Architecture](<img width="1536" height="1024" alt="Aricheturce" src="https://github.com/user-attachments/assets/ca851fd5-a86c-4fa4-9fef-cd33c993c084" />
)


### Streamlit Dashboard
![Dashboard](<img width="959" height="427" alt="DashBoard" src="https://github.com/user-attachments/assets/9e404b58-5fd1-4e52-9550-25acb9eabf58" />
)

### Result
![Result](<img width="955" height="422" alt="Result" src="https://github.com/user-attachments/assets/83810ebd-1a0b-45b7-b577-5d3277e3b379" />
)
