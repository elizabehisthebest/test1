import joblib

def predict(data):
 clf = joblib.load('clf_model.sav')
 return clf.predict(data)