import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Find the .env file
ENV_PATH = BASE_DIR / ".env"


# Load environment variables
load_dotenv(dotenv_path=ENV_PATH, override=True)


# Get OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# Check whether the API key exists
if not OPENROUTER_API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY was not found. Check your .env file."
    )


def create_dataset_context(df):

    # Get the first 10 rows
    sample_data = df.head(10).to_string()


    # Create dataset information for the AI
    context = f"""
    Dataset Shape:
    {df.shape}

    Column Names:
    {list(df.columns)}

    Data Types:
    {df.dtypes.astype(str).to_string()}

    Missing Values:
    {df.isnull().sum().to_string()}

    Statistical Summary:
    {df.describe(include='all').to_string()}

    Sample Data:
    {sample_data}
"""

    return context


def ask_ai(df, question):

    # Create dataset context
    context = create_dataset_context(df)


    # Create the prompt
    prompt = f"""
    You are an expert Data Analyst.

    You are given information about a dataset.

    Your task is to answer the user's question based only on
    the provided dataset information.

    IMPORTANT RULES:

    1. Use only the provided dataset information.
    2. Do not invent facts or values.
    3. If information is unavailable, clearly say so.
    4. Give clear and professional answers.
    5. Explain insights in simple language.
    6. Provide useful business insights when possible.

    DATASET INFORMATION:

    {context}

    USER QUESTION:

    {question}
"""


    # OpenRouter API URL
    url = "https://openrouter.ai/api/v1/chat/completions"


    # Request headers
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }


    # Request data
    data = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }


    # Send request to OpenRouter
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=60
    )


    # Raise an error if the request fails
    response.raise_for_status()


    # Convert response into JSON
    result = response.json()


    # Return the AI-generated answer
    return result["choices"][0]["message"]["content"]