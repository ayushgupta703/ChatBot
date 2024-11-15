# AI Chatbot Assistant

This is a simple AI-based chatbot built using LangChain, Streamlit, and Google's Generative Language API. The chatbot is designed to respond to user queries in natural language and provide relevant information based on the input.

## Features

- **Natural Language Understanding:** The chatbot can understand and respond to queries in English.
- **Real-time Chat:** It streams the chatbot's responses in real-time as the model generates them.
- **Google's Generative Language API:** The chatbot uses Google's Gemini 1.5 Flash model for generating responses.
- **Session Persistence:** Chat history is maintained throughout the session for context-aware responses.
- **Secure Service Account Integration:** The chatbot integrates securely with Google's Generative Language API using service account credentials.

## Requirements

- Python 3.7 or higher
- Google Cloud Service Account JSON file
- **Google Cloud APIs**: Dialogflow API and Gemini API must be enabled
- LangChain, Streamlit, and necessary dependencies

## Setup Instructions

### 1. Enable APIs
Go to the [Google Cloud Console](https://console.developers.google.com/):
- Enable the **Dialogflow API** and **Gemini API** for your Google Cloud project.

### 2. Generate Service Account Credentials
To integrate the Google APIs with your chatbot, you'll need to create a **Service Account** with the necessary permissions:
- In the Google Cloud Console, go to **IAM & Admin > Service Accounts**.
- Create a new service account and grant it the required roles for Dialogflow and Gemini API access.
- Download the **JSON key** for the service account.

### 3. Set Up the Service Account JSON Key
Once you have the **JSON key file**, place it in the project directory or a preferred location. 
- Update the path to the JSON file in **line 28** of the `chatbot.py` code. Change the value of `credentials_path` to the correct file path:
  ```python
  credentials_path = "C:\\path\\to\\your\\service_account_file.json"
  ```

### 4. Install Dependencies
Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Once you've set up the environment and installed dependencies, you can run the chatbot by executing:
```bash
streamlit run chatbot.py
```

---
