AI Chat Bot
This is a simple console-based chatbot built with Python and the Google Gemini API. This project is intended to be the backend for a Telegram bot.

Features
Communicates with the Google Gemini API to generate responses.

Provides a conversational interface in the console.

Prerequisites
To run this project, you need:

Python 3.8 or higher.

A Google AI Studio API key.

Setup and Installation
Clone the repository:

git clone [https://github.com/your-username/AI-CHAT-bot.git](https://github.com/your-username/AI-CHAT-bot.git)
cd AI-CHAT-bot

Install dependencies:
This project uses a requirements.txt file to manage its dependencies. To install them, run the following command:

pip install -r requirements.txt

Set your API key:
The program uses an environment variable to securely access your API key. Do not hardcode your API key in the code.

On Linux/macOS:

export GEMINI_API_KEY='your_api_key_here'

On Windows:

set GEMINI_API_KEY=your_api_key_here

Replace your_api_key_here with your actual API key.

Usage
Once you have completed the setup, you can run the chatbot from your terminal:

python chatbot.py

You can now start a conversation with the AI. Type exit or quit to end the chat.

Next Steps
This repository will be used to create a Telegram bot. The chatbot.py file will be the core logic for handling the AI's responses.
