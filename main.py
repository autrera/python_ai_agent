import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

parameters = sys.argv[1:]
prompt = parameters[0] if len(parameters) > 0 else ""

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    if prompt == "":
        print("A prompt needs to be provided!")
        exit(1)

    print("Hello from python-ai-agent!")
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()
