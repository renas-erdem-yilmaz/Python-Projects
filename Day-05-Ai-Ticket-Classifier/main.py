import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = pd.read_csv("tickets.csv")

X = data["message"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print("Model accuracy:", round(accuracy * 100, 2), "%")

print("\n--- TEST RESULTS ---")

for message, real, predicted in zip(X_test, y_test, predictions):
    print("\nMessage:", message)
    print("Real:", real)
    print("Predicted:", predicted)

feature_names = vectorizer.get_feature_names_out()

print("\n--- LEARNED FEATURES ---")

for i, class_name in enumerate(model.classes_):
    top_indices = model.coef_[i].argsort()[-8:][::-1]

    print(f"\nTop words for {class_name}:")

    for index in top_indices:
        print(feature_names[index], round(model.coef_[i][index], 3))

print("\n--- AI SUPPORT CLASSIFIER ---")
print("Type 'exit' to stop.")

while True:
    user_message = input("\nEnter a support message: ")

    if user_message.lower() == "exit":
        break

    vectorized_message = vectorizer.transform([user_message])

    prediction = model.predict(vectorized_message)[0]
    probabilities = model.predict_proba(vectorized_message)[0]

    confidence = max(probabilities)

    if confidence < 0.45:
        print("\nPrediction: uncertain")
        print("Confidence:", round(confidence * 100, 2), "%")
    else:
        print("\nPrediction:", prediction)
        print("Confidence:", round(confidence * 100, 2), "%")