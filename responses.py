def get_response(emotion):
    responses = {
        "happy": "That's great 😊",
        "sad": "I'm here for you 💙",
        "angry": "Take a deep breath 🌿",
        "neutral": "Tell me more 🙂"
    }

    return responses.get(emotion, "I'm here to listen 💙")