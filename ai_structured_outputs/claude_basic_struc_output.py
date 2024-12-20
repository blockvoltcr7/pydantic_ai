import os
from typing import List

from anthropic import Anthropic
from pydantic import BaseModel, Field


# Define a simple Pydantic model for the response structure
class MovieReview(BaseModel):
    """
    A Pydantic model representing a movie review.

    Attributes:
        title (str): The title of the movie being reviewed.
        rating (int): Rating out of 5 stars, must be between 1 and 5.
        pros (List[str]): List of positive aspects of the movie.
        cons (List[str]): List of negative aspects of the movie.
    """

    title: str = Field(description="The title of the movie being reviewed")
    rating: int = Field(description="Rating out of 5 stars", ge=1, le=5)
    pros: List[str] = Field(description="List of positive aspects of the movie")
    cons: List[str] = Field(description="List of negative aspects of the movie")


def get_api_key() -> str:
    """
    Get API key from environment variables, checking both possible names.

    Raises:
        ValueError: If neither CLAUDE_API_KEY nor ANTHROPIC_API_KEY is set.

    Returns:
        str: The API key for accessing the Anthropic client.
    """
    api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "Please set either CLAUDE_API_KEY or ANTHROPIC_API_KEY environment variable"
        )
    return api_key


# Initialize Anthropic client
client = Anthropic(api_key=get_api_key())

# Example movie review text
movie_review = """
Avatar was a visually stunning movie with groundbreaking special effects. 
The world of Pandora was beautiful and immersive. However, the plot was somewhat 
predictable and the runtime was quite long. Overall I'd give it 4 out of 5 stars.
"""

try:
    # Create message with structured output
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": (
                    "Analyze this movie review and output a JSON object with the following fields:\n"
                    "- title: the movie title\n"
                    "- rating: rating out of 5\n"
                    "- pros: list of positive points\n"
                    "- cons: list of negative points\n\n"
                    f"Review: {movie_review}"
                ),
            }
        ],
        system="Always respond with valid JSON that matches the MovieReview schema.",
    )

    # Extract the raw JSON string from Claude's response
    json_str = message.content[0].text

    # Parse response into Pydantic model
    review = MovieReview.model_validate_json(json_str)
    review_json_dump = MovieReview.model_dump_json(review)

    print(f"review json dump: {review_json_dump}")

    print(f"review json: {review}")
    # Print the structured output
    print(f"Movie: {review.title}")
    print(f"Rating: {review.rating}/5")
    print("\nPros:")
    for pro in review.pros:
        print(f"- {pro}")
    print("\nCons:")
    for con in review.cons:
        print(f"- {con}")

except Exception as e:
    print(f"Error: {str(e)}")
