
import pandas as pd
import numpy as np
import pickle

# Load trained model (make sure model.pkl exists in the correct location)
with open('prediction_app/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example: Features used by model (update according to your model input)
model_features = ['Open', 'High', 'Low', 'Close', 'Volume']

def predict_crypto(input_data):
    '''
    input_data: dict with keys matching model_features
    returns: prediction result
    '''
    try:
        df = pd.DataFrame([input_data], columns=model_features)
        prediction = model.predict(df)
        return prediction[0]
    except Exception as e:
        return f"Error during prediction: {str(e)}"
