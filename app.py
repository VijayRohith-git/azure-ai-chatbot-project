import os
import re
from typing import Optional

try:
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
except ImportError:  # pragma: no cover - optional dependency
    TextAnalyticsClient = None
    AzureKeyCredential = None

class Chatbot:
    def __init__(self) -> None:
        self.client = self._build_client()

    def _build_client(self):
        if TextAnalyticsClient is None or AzureKeyCredential is None:
            return None
        endpoint = os.getenv("AZURE_AI_ENDPOINT")
        key = os.getenv("AZURE_AI_KEY")
        if not endpoint or not key:
            return None
        return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    def get_response(self, user_input: str) -> str:
        cleaned = (user_input or "").strip()
        if not cleaned:
            return "I did not receive a message. Please try again."

        if re.search(r"\b(help|capabilit|features|what can you do)\b", cleaned, re.I):
            return (
                "My capabilities include greeting users, answering simple questions, "
                "analyzing sentiment, and explaining how this project connects a chatbot "
                "to Azure AI Services."
            )

        if re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", cleaned, re.I):
            return "Hello! I am your Azure-enabled chatbot. Ask me something or type 'help' to see my capabilities."

        if re.search(r"\b(sentiment|feeling|mood|emotion)\b", cleaned, re.I):
            sentiment = self._analyze_sentiment(cleaned)
            return f"Sentiment analysis suggests: {sentiment}."

        if re.search(r"\b(azure|ai service|cloud|language service)\b", cleaned, re.I):
            return "This chatbot is connected to Azure AI Language for sentiment analysis when credentials are configured."

        if re.search(r"\b(why|what|when|where|how)\b", cleaned, re.I):
            return "I can provide a brief explanation. For example, ask me about Azure AI, this project, or sentiment analysis."

        return "I can help with greetings, general questions, and sentiment analysis. Try asking me something else."

    def _analyze_sentiment(self, text: str) -> str:
        if self.client is None:
            return self._fallback_sentiment(text)
        try:
            response = self.client.analyze_sentiment(documents=[text])[0]
            if response.sentiment == "positive":
                return "positive"
            if response.sentiment == "negative":
                return "negative"
            return "neutral"
        except Exception:
            return self._fallback_sentiment(text)

    def _fallback_sentiment(self, text: str) -> str:
        lowered = text.lower()
        positive_words = ["good", "great", "love", "happy", "excellent", "awesome", "wonderful"]
        negative_words = ["bad", "angry", "hate", "sad", "terrible", "awful", "poor"]
        positive_count = sum(1 for word in positive_words if word in lowered)
        negative_count = sum(1 for word in negative_words if word in lowered)
        if positive_count > negative_count:
            return "positive"
        if negative_count > positive_count:
            return "negative"
        return "neutral"

def main() -> None:
    chatbot = Chatbot()
    print("Azure AI Chatbot ready. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        print("Bot:", chatbot.get_response(user_input))

if __name__ == "__main__":
    main()