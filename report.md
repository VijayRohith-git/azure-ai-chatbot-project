# Integrating a Traditional Chatbot with Azure AI Services

## Abstract
This project created a simple chatbot that extends a traditional rule-based conversational interface with Azure AI Language sentiment analysis. The chatbot can respond to multiple prompts, explain its capabilities, and handle malformed or empty input. The work demonstrates how a basic chatbot can be enhanced with a cloud-based AI-as-a-service offering while remaining accessible and practical for free-tier use.

## Introduction
The assignment required the development of a chatbot that integrates a managed AI service, uses the free tier of Azure AI Services when possible, and documents the development process in a report. The project was built as a Python application that can operate with Azure AI Language for sentiment analysis when credentials are configured, while also providing a local fallback for testing and demonstration.

## Project Development
The project began by creating a simple chatbot that could respond to greetings, explain its capabilities, and return a useful message for empty or malformed input. The next step involved adding a sentiment analysis feature by using the Azure AI Language SDK. The implementation uses environment variables for the Azure endpoint and key so sensitive credentials are not hardcoded into the source code. When those values are missing, the application falls back to a lightweight local heuristic that still provides a meaningful result.

## Challenges and Lessons Learned
One challenge was ensuring the chatbot remained functional even when Azure credentials were unavailable. This was important because the free-tier setup may require account configuration and service provisioning before the service can be used. Another challenge was keeping the project simple enough to be understandable while still demonstrating a realistic Azure AI integration. The main lesson learned was that cloud-based AI services should be introduced as an enhancement layer rather than as a requirement for every local test. This design makes the project more reliable and easier to demonstrate.

## Interesting and Exciting Aspects
The most interesting part of the project was seeing the chatbot transition from a basic rule-based experience to one that could interpret sentiment from user input. The integration with Azure AI Services made the project feel more realistic and closer to production-style AI applications. The use of environment variables and fallback logic also made the implementation more robust and professional.

## Areas for Improvement
The current version is intentionally simple and could be improved by adding richer conversation flows, better error handling, and more sophisticated prompt responses. A future version could also provide a polished web interface or support additional Azure AI services such as summarization or named entity recognition. The project would also benefit from more extensive testing and a more complete deployment workflow.

## AI Disclosure
Artificial intelligence tools were used during the creation of this project and report. A generative AI assistant was used to help structure the code, draft the report content, and refine the explanation of the Azure integration. Any AI-generated content was reviewed, edited, and adapted to ensure it matched the assignment requirements and the actual implementation.

## Conclusion
This project successfully demonstrated how a traditional chatbot can be connected to Azure AI Services using the free tier of Azure AI Language. The experience highlighted both the power of cloud-based AI services and the importance of designing systems that remain useful even when the external service is unavailable. The final result is a practical chatbot that is easy to run, easy to extend, and aligned with the goals of the assignment.

## References
Microsoft. (n.d.). Azure AI Language. https://learn.microsoft.com/azure/ai-services/language/
Microsoft. (n.d.). Azure AI Services pricing. https://azure.microsoft.com/pricing/details/cognitive-services/
