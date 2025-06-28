import os

from dotenv import load_dotenv
from google import genai

load_dotenv(".env")
SECRET_KEY = "SAD@#REFGSDFQWFEWGASRG3254t$%#$dsgAS"


def main():
    client = genai.Client(api_key=os.environ.get("SECRET_KEY"))
    question = "Why is the sky blue?"
    model = "gemini-2.0-flash-001"

    response = client.models.generate_content(model=model, contents=question)
    print(response.text)


if __name__ == "__main__":
    main()
