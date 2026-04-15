import random

supportive_openers = [
    "I’m really glad you shared that.",
    "Thank you for trusting me with how you feel.",
    "I hear you.",
    "That sounds meaningful.",
    "I appreciate you opening up."
]

emotion_support = {

    "sad":[
        "It sounds like you're going through a heavy moment.", 
        "Sadness can feel really draining sometimes.",
        "I'm sorry you're feeling this way."
    ],

    "angry":[
        "It seems something really upset you.",
        "That sounds frustrating.",
        "I can sense strong emotions there."
    ],

    "happy":[
        "That’s really lovely to hear.",
        "I’m glad something positive is happening for you.",
        "It sounds like things are going well."
    ],

    "anxious":[
        "That sounds stressful.",
        "Anxiety can feel overwhelming, especially when thoughts race.",
        "It seems like something is weighing on your mind."
    ],

    "neutral":[
    "I’d like to understand better how you're feeling.",
    "Tell me a little more about what's on your mind.",
    "I'm here and listening carefully.",
    "What’s been going through your thoughts lately?",
    "It sounds like there’s more you might want to share."
]
}

coping_suggestions = {

    "sad":[
    "Sometimes talking it out can help lighten the feeling.",
    "Being gentle with yourself right now might help.",
    "You don't have to go through this alone.",
    "Would you like to talk about what's making you feel this way?"
],

    "angry":[
        "Taking slow breaths might help settle the intensity.",
        "Stepping away for a moment can sometimes help clear the mind.",
        "Channeling that energy into something physical can help."
    ],

    "anxious":[
        "Try taking one slow deep breath with me.",
        "Grounding yourself in your surroundings might help.",
        "Focusing on what you can control can sometimes ease anxiety."
    ],


    "happy":[
        "It’s nice to notice and appreciate moments like this.",
        "Savoring positive moments can be really powerful.",
        "What do you think contributed to this feeling?"
    ]
}

followups = [
    "Would you like to tell me more?",
    "I'm here to listen.",
    "What’s been on your mind lately?",
    "Do you want to share a bit more about that?"
]


def get_response(emotion):

    if emotion == "neutral":
        opener = "I'm here with you."

    opener = random.choice(supportive_openers)
    main = random.choice(emotion_support.get(emotion, ["I'm here with you."]))
    support = random.choice(coping_suggestions.get(emotion, ["Take your time."]))
    end = random.choice(followups)

    return f"{opener} {main} {support} {end} (Detected emotion: {emotion})" 