import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "app.py"

spec = importlib.util.spec_from_file_location("app_module", APP_PATH)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


def test_help_response():
    chatbot = app_module.Chatbot()
    response = chatbot.get_response("help")
    assert "capabilities" in response.lower()


def test_empty_input_response():
    chatbot = app_module.Chatbot()
    response = chatbot.get_response("   ")
    assert "did not receive" in response.lower()


def test_sentiment_fallback():
    chatbot = app_module.Chatbot()
    response = chatbot.get_response("I am feeling great today")
    assert "positive" in response.lower()
