import requests
from utils.env_loader import API_KEY, API_URL

def get_destination(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-Title": "AI Travel Designer"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct", 
        "messages": [
            {"role": "system", "content": "You are a helpful travel assistant. Suggest a great travel destination based on user's mood or interest."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        destination = response.json()['choices'][0]['message']['content']
        return destination.strip()
    else:
        return "Sorry, couldn't fetch a destination. Please try again."
