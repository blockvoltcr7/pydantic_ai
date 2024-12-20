# AI Structured Output Examples

This project demonstrates different approaches to generating and handling structured outputs from various AI models (OpenAI, Claude, and Gemini) using Python. It includes examples of working with LangChain and implementing structured data validation using Pydantic.

## Project Structure

```
.
├── ai_structured_outputs/
│   ├── claude_basic_struc_output.py    # Claude AI structured output example
│   ├── gemini_basic_struc_output.py    # Gemini AI structured output example
│   └── openai_basic_struc_output.py    # OpenAI structured output example
├── langsmith/
│   └── langsmith_starter.py            # Basic LangChain example
└── basics/
    ├── __init__.py
    └── sample_pydantic.py              # Basic Pydantic usage example
```

## Features

- **Structured Output Generation**: Examples of generating structured JSON outputs from different AI models
- **Pydantic Integration**: Data validation and serialization using Pydantic models
- **Multiple AI Providers**: Support for:
  - OpenAI (GPT-4)
  - Anthropic (Claude)
  - Google (Gemini)
- **LangChain Integration**: Basic example of using LangChain with OpenAI

## Requirements

```
anthropic
google-generativeai
langchain
langchain-openai
openai
pydantic
```

## Environment Variables

The following environment variables need to be set:

- `OPENAI_API_KEY` - For OpenAI integration
- `CLAUDE_API_KEY` or `ANTHROPIC_API_KEY` - For Claude integration
- `GEMINI_API_KEY` - For Gemini integration

## Examples

### Basic Pydantic Usage
```python
from basics.sample_pydantic import User

user = User(name="John", age=30)
print(user.model_dump_json())s
```

### OpenAI Structured Output
Generates structured summaries with keywords using GPT-4.

### Claude Movie Review
Generates structured movie reviews with ratings, pros, and cons.

### Gemini City Information
Provides structured information about cities including population and description.

### LangSmith Starter
Basic example of using LangChain with OpenAI's chat models.

## Getting Started

1. Clone the repository
2. Install the required dependencies
3. Set up your environment variables
4. Run any of the example files to see them in action

