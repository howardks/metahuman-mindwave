import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import joblib

# Load the EEG data
df = pd.read_csv('test.csv')

# Synthetic Emotion Label Generation based on EEG Features
# This function synthesizes emotion labels based on the heuristic understanding of the EEG features.

# Define the function to generate emotion labels
def generate_emotion_labels(row):
    # Enhanced logic for assigning labels based on EEG features
      # Conditions for determining emotion labels based on EEG features
    conditions = [
        # Very negative: High delta, indicating sleepiness or disengagement
        (df['delta'] > df[['lowAlpha', 'highAlpha', 'lowBeta', 'highBeta']].sum(axis=1)),
        # Negative: High beta, suggesting stress or anxiety
        ((df['lowBeta'] + df['highBeta']) > df[['lowAlpha', 'highAlpha']].sum(axis=1)),
        # Neutral: Balanced alpha and beta, indicating a normal state of relaxation or alertness
        ((df['lowAlpha'] + df['highAlpha']) > df['theta']) & ((df['lowAlpha'] + df['highAlpha']) < (df['lowBeta'] + df['highBeta'])),
        # Positive: High alpha, indicating relaxation or meditative state
        ((df['lowAlpha'] + df['highAlpha']) > (df['lowBeta'] + df['highBeta'])),
        # Very Positive: High gamma, suggesting intense mental activity or engagement
        (df['highGamma'] > df['lowGamma']),
    ]
    choices = ['very negative', 'negative', 'neutral', 'positive', 'very positive']
    # Apply conditions
    df['emotion_label'] = np.select(conditions, choices, default='neutral')
    return df['emotion_label']

# Apply the function to generate labels
df['emotion_label'] = generate_emotion_labels(df)

# Split the data into features and target
X = df[['delta', 'theta', 'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'highGamma']]
y = df['emotion_label']

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predict on the test data
y_pred = model.predict(X_test_scaled)

# Print out the performance metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model and scaler
joblib.dump(model, 'trained_emotion_model.pkl')
joblib.dump(scaler, 'emotion_scaler.pkl')

print("Model and scaler have been saved.")
