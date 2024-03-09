import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Correctly import numpy at the beginning of your script
import numpy as np

# Load the EEG dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Preprocess the data
def preprocess_data(df):
    # Convert 'NA' strings to np.nan for numeric conversion
    df.replace('NA', np.nan, inplace=True)
    df.replace(' X*', np.nan, inplace=True)  # Assuming ' X*' is not a valid entry for numeric columns

    # Convert columns to numeric, ensuring 'NA' values are handled
    numeric_cols = [' Delta', ' Theta', ' Alpha1', ' Alpha2', ' Beta1', ' Beta2', ' Gamma1', ' Gamma2', ' Attention', ' Meditation']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing values with the mean of each column
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    return df

# Define the Emotion Interpretation Function with Happiness included
def interpret_emotion(row):
    # Define thresholds for EEG wave activity criteria
    # Note: These thresholds are placeholders and should be defined based on empirical data or domain knowledge
    if row[' Beta1'] + row[' Beta2'] > 100000:  # Placeholder threshold
        return 'Anger'
    elif row[' Alpha1'] + row[' Alpha2'] > 50000:  # Placeholder threshold
        return 'Sadness'
    elif row[' Gamma1'] + row[' Gamma2'] > 20000:  # Placeholder threshold
        return 'Attention'
    elif row[' Theta'] > 30000:  # Placeholder threshold
        return 'Meditation'
    elif row[' Delta'] > 40000:  # Placeholder threshold
        return 'Confusion'
    else:
        return 'Happiness'  # Default to Happiness if no other condition is met

# Main function to run the program
def main():
    file_path = 'MindwaveConnection.py'  # Update this path to your actual CSV file location
    df = load_data(file_path)
    df = preprocess_data(df)
    
    # Apply the emotion interpretation function
    df['Interpreted_Emotion'] = df.apply(interpret_emotion, axis=1)
    
    # Display the distribution of interpreted emotions
    print(df['Interpreted_Emotion'].value_counts())

if __name__ == "__main__":
    main()
