import os
from typing import Optional

import google.generativeai as genai
from pydantic import BaseModel, Field


# Define Pydantic model for city information
class CityInfo(BaseModel):
    city_name: str = Field(description="The name of the city")
    country: str = Field(description="The country where the city is located")
    is_capital: bool = Field(description="Whether the city is a capital")
    population: Optional[int] = Field(
        description="Approximate population of the city", default=None
    )
    description: str = Field(description="Brief description of the city's significance")


# Configure Gemini AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model with configuration
generation_config = {
    "temperature": 0.1,  # Lower for more factual responses
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",  # Specify JSON output
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start chat session
chat_session = model.start_chat(history=[])

# Prompt template for structured output
prompt = """
Provide information about the capital of Morocco with these fields:
- city_name: name of the city
- country: country name
- is_capital: boolean indicating if it's a capital
- population: approximate population number
- description: brief description of the city's significance

Respond with only the JSON object.
"""

# Send message and get response
response = chat_session.send_message(prompt)

# Parse response into Pydantic model
try:
    city_info = CityInfo.model_validate_json(response.text)

    # Print formatted output
    print(f"\nCity Information:")
    print(f"Name: {city_info.city_name}")
    print(f"Country: {city_info.country}")
    print(f"Capital: {'Yes' if city_info.is_capital else 'No'}")
    if city_info.population:
        print(f"Population: {city_info.population:,}")
    print(f"Description: {city_info.description}")

except Exception as e:
    print(f"Error parsing response: {e}")
    print("Raw response:", response.text)
