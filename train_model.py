from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.makedirs("saved_model", exist_ok=True)

iris = load_iris()

X = iris.data
y = iris.target

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "saved_model/model.pkl")

print("Model saved successfully.")