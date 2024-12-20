import json
import os

from openai import OpenAI
from pydantic import BaseModel, ValidationError


# Define a structured output schema using Pydantic
class StructuredOutput(BaseModel):
    summary: str
    keywords: list[str]


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_structured_output(prompt: str) -> StructuredOutput:
    try:
        # Call the OpenAI API to generate a response with streaming
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that generates structured summaries.",
                },
                {"role": "user", "content": prompt},
            ],
            stream=True,
        )

        # Initialize variables to collect the streamed response
        collected_messages = []

        # Iterate through the streamed response
        for chunk in response:
            chunk_message = chunk.choices[0].delta.content or ""
            collected_messages.append(chunk_message)

        # Combine the collected messages into a single response
        full_reply_content = "".join(collected_messages)

        # Parse the JSON response
        response_data = json.loads(full_reply_content)

        # Validate and parse the response into the structured output format
        structured_data = StructuredOutput(**response_data)
        return structured_data

    except ValidationError as e:
        print("Validation error:", e)
        raise
    except Exception as e:
        print("OpenAI API error:", e)
        raise
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        raise


# Example usage
if __name__ == "__main__":
    user_prompt = (
        "Summarize the importance of AI in modern technology and provide three key keywords related to AI. "
        "Respond in JSON format with fields 'summary' and 'keywords'."
    )

    try:
        structured_output = generate_structured_output(user_prompt)
        print("Structured Output:")
        print(structured_output.model_dump_json(indent=4))
    except Exception as e:
        print("An error occurred:", e)
