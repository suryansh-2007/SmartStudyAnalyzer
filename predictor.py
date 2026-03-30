import joblib
import numpy as np

def predict_marks(study_hrs, sleep_hrs, att, prev_marks, subject):
    """Predict student marks - LIVE DEMO"""
    print(f"\n Predicting for:")
    print(f"   Study: {study_hrs}hrs | Sleep: {sleep_hrs}hrs")
    print(f"   Attendance: {att}% | Previous: {prev_marks}%")
    print(f"   Subject: {subject}")
    
    # Load model
    model = joblib.load('study_model.pkl')
    le = joblib.load('label_encoder.pkl')
    
    # Predict
    subject_code = le.transform([subject])[0]
    data = np.array([[study_hrs, sleep_hrs, att, prev_marks, subject_code]])
    marks = model.predict(data)[0]
    
    # Risk analysis
    if marks < 40:
        risk = " HIGH RISK - FAIL"
    elif marks < 60:
        risk = " MEDIUM RISK"
    else:
        risk = " LOW RISK - PASS"
    
    print(f" PREDICTED MARKS: {marks:.1f}%")
    print(f" STATUS: {risk}")
    print("-" * 40)
    
    return marks

# Quick test
if __name__ == "__main__":
    predict_marks(1.5, 8, 70, 55, 'Math')     # Lazy student
    predict_marks(4, 7, 90, 80, 'Science')   # Good student