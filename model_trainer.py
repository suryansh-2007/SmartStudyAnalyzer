import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model():
    print(" Training ML Model...")
    df = pd.read_csv('student_data.csv')
    
    # Encode subjects
    le = LabelEncoder()
    df['Subject_Code'] = le.fit_transform(df['Subject'])
    
    # Features & Target
    X = df[['Study_Hours', 'Sleep_Hours', 'Attendance', 'Previous_Marks', 'Subject_Code']]
    y = df['Final_Marks']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    score = model.score(X_test, y_test)
    
    # SAVE MODEL
    joblib.dump(model, 'study_model.pkl')
    joblib.dump(le, 'label_encoder.pkl')
    
    print(f" Model trained! R² Score: {score:.3f}")
    print(" Saved: study_model.pkl + label_encoder.pkl")
    print(" Feature Importance:")
    for i, imp in enumerate(model.feature_importances_):
        print(f"   {['Study','Sleep','Att','Prev','Sub'][i]}: {imp:.2f}")
    
    return model.score(X_test, y_test)

if __name__ == "__main__":
    train_model()