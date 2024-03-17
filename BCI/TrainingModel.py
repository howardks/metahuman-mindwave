import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the EEG data
df = pd.read_csv('test.csv')

# Synthetic Emotion Label Generation based on EEG Features
# This function synthesizes emotion labels based on the heuristic understanding of the EEG features.

def generate_emotion_labels(row):
    if row['attention'] > 75 and row['meditation'] > 75:
        return 'very positive'
    elif row['attention'] > 50 or row['meditation'] > 50:
        return 'positive'
    elif row['lowAlpha'] > row['highBeta'] and row['lowBeta'] > row['highAlpha']:
        return 'neutral'
    elif row['delta'] > row['theta'] and row['lowGamma'] > row['highGamma']:
        return 'negative'
    else:
        return 'very negative'

df['emotion_label'] = df.apply(generate_emotion_labels, axis=1)

# Preparing the dataset
X = df[['attention', 'meditation', 'delta', 'theta', 'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'highGamma']]
y = df['emotion_label']

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training: RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Model Evaluation
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))

# Save the model and scaler
joblib.dump(model, 'trained_emotion_model.pkl')
joblib.dump(scaler, 'emotion_scaler.pkl')

print("Model and scaler have been saved.")
