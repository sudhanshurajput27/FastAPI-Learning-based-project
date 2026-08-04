import joblib

model = joblib.load("app/models/iris_model.pkl")

flower_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

def make_prediction(data):

    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]]

    prediction = model.predict(features)

    return flower_names[prediction[0]]