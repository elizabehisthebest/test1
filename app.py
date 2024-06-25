import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict



st.title("Heart Disease Prediction")
st.image('12.jpg', caption='Use as refrence')

age = st.slider("age", 1, 100)

sex = st.slider("sex", 0, 1)

trestps = st.slider("trestps", 80, 240)

chol = st.slider("chol", 100, 600)

fbs = st.slider("fbs", 0, 1)

restecg = st.slider("restecg", 0, 2)

thalach = st.slider("thalach", 40, 250)

exang = st.slider("exang", 0, 1)

oldpeak = st.slider("oldpeak", 0.0, 8.0)

slope = st.slider("slope", 0, 2)

ca = st.slider("ca", 0, 4)

cp = st.slider("cp", 0, 3)


thal = st.slider("thal", 0, 3)

test= st.button("Predict Heart Disease")         


if test: 
      result = predict(np.array([[age,sex,trestps,thal,fbs,exang,oldpeak,chol,restecg,slope,thalach,ca,cp]]))
      st.text(result[0])

