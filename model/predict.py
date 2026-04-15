import pickle
from model.preprocess import clean_text

model = pickle.load(open("model/emotion_model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

def predict_emotion(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return prediction