import numpy as np
import pandas as pd
import joblib



class EmotionDetection:
    def __init__(self, model_path='trained_emotion_model', scaler_path='emotion_scaler.pkl'):
        # Load the model and scaler
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.class_names = ['very negative', 'negative', 'neutral', 'positive', 'very positive']
        
    def preprocess_data(self, df):
        # Preprocess the data
        # Ensure df has the correct columns here
        feature_columns = ['delta', 'theta', 'lowAlpha', 'highAlpha',
                           'lowBeta', 'highBeta', 'lowGamma', 'highGamma']
        # Select and reorder columns as necessary to match training data
        selected_df = df[feature_columns]
        scaled_features = self.scaler.transform(selected_df)
        return scaled_features
    
    def predict_emotion(self, processed_data):
        # Predict emotional states using the model
        # Predict emotional states using the model
        predictions = self.model.predict(processed_data)
        predicted_states = [self.class_names[pred] for pred in predictions]
        return predicted_states


