# Azure AI Chatbot Project

This project builds a simple chatbot that can respond to multiple prompts, explain its capabilities, and gracefully handle malformed input. It uses Azure AI Language sentiment analysis when credentials are configured, and falls back to a local heuristic when they are not.

## Features
- Responds to greetings and general questions
- Lists supported capabilities
- Handles malformed or empty input
- Uses Azure AI Language sentiment analysis when endpoint and key are available
- Supports a local fallback for offline or demo use

## Setup
1. Create a Python virtual environment.
2. Install requirements: `pip install -r requirements.txt`
3. Set environment variables:
   - `AZURE_AI_ENDPOINT`
   - `AZURE_AI_KEY`
4. Run the chatbot: `python app.py`

## Notes
This project is designed to work with the free tier of Azure AI Services where available, while still being usable without credentials for local testing.
