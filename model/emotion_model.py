import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from preprocess import clean_text

# load dataset
data = pd.read_csv("data/emotions.csv")

# clean text
data["clean_text"] = data["text"].apply(clean_text)

# vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["clean_text"])
y = data["emotion"]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# save
pickle.dump(model, open("model/emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model trained successfully")