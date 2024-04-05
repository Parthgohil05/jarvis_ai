from config import key  
import requests  
from  mic_to_text import mic1

def chat1(chat):
    messages = []

    # Initial system message
    system_message = "You are an AI bot, your name is Jarvis."
    message = {
        "role": "user",
        "parts": [{"text": system_message + " " + chat}]
    }
    messages.append(message)

    # Creating data to be sent to the language model API
    data = {"contents": messages}

    # URL for the language model API
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + key

    # Making a POST request to the language model API
    response = requests.post(url, json=data)
    
    t1 = response.json()
    #print(t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

# Example usage
chat = mic1()
chat1(chat)
