#install the packages with: pip install pandas nltk scikit-learn
import pandas as pd
import re
import nltk #Natural Language Toolkit: text processing library

from sklearn.model_selection import train_test_split #splits training data into test data
from sklearn.feature_extraction.text import TfidfVectorizer #converts text to numbers
from sklearn.naive_bayes import MultinomialNB #the machine learning model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report #used to evaluate the model

from nltk.corpus import stopwords

# Download stopwords (only needed first time)
#nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# ----------------------------
# 1 Load dataset
# ----------------------------

data = pd.read_csv(r"C:\Users\MTill\Documents\Git repository\PythonExercises\Dataset_10191.csv")

texts = data["TEXT"]
labels = data["LABEL"]

labels = labels.replace({
    "ham": "safe",
    "spam": "spam",
    "smishing": "phishing"
})

# ----------------------------
# 2 Text preprocessing
# ----------------------------

def preprocess(text):

    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^a-z\s]", "", text) # remove symbols

    words = text.split()

    words = [w for w in words if w not in stop_words]

    return " ".join(words)

texts_clean = texts.apply(preprocess)

# ----------------------------
# 3 Convert text to numbers
# ----------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts_clean)
y = labels

# ----------------------------
# 4 Train / Test split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# 5 Train model
# ----------------------------

models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# ----------------------------
# 6 Evaluate model
# ----------------------------

for name, model in models.items():
    print(f"\n--- {name} ---")

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))

# ----------------------------
# 7 Test with a new email
# ----------------------------

def predict_email(email_text):
    clean = preprocess(email_text)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)[0]
    return prediction

# Example test
'''print("Enter email (press ENTER twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

email = "\n".join(lines)
result = predict_email(email)
print("Prediction:", result)'''