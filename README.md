# Langchain Chat using GROQ
This project allows users to interact with a chatbot powered by Langchain and GROQ using a custom-built Streamlit web app. The chatbot uses the llama-3.3-70b-versatile model to respond to user inputs. The project leverages the Langchain API and GROQ API to generate responses dynamically.

![{F063A971-5258-4BB9-9303-C01835813117}](https://github.com/user-attachments/assets/9638c174-bc8f-44f8-933e-b79c12dd7483)


## Requirements
Before running this project, ensure you have the following:
- Python 3.7 or later
- Required Python libraries (listed in requirements.txt)
- You will also need to create a .env file to securely store your GROQ API key.

## Setup Instructions
1. Clone the repository
  Clone this repository to your local machine:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Install required dependencies
   Install all necessary Python libraries using pip:
  ```bash
  pip install -r requirements.txt
  ```
The required libraries include:
  - streamlit for building the web app
  - langchain-groq for integrating with the GROQ API
  - python-dotenv for loading environment variables from a .env file
  - requests and json for API responses

3. Setup environment variables
  Create a .env file in the root directory of your project. Add your GROQ API key like so:
  ```GROQ_API_KEY=<your_groq_api_key>```

4. Run the application
  Run the Streamlit app:
  ```streamlit run app.py```
  This will open the web app in your default browser.

5. Usage
  Once the application is running, you will be presented with a chat interface where you can type your messages. The app stores the chat history, and each message you send is processed by the llama-3.3-70b-versatile model via the GROQ API. The assistant's response will be displayed below your message in the chat window.

## Key Features
Chat History: The chat history is stored in the session state so that each new message is appended to the conversation. This creates a more seamless interaction with the assistant.
