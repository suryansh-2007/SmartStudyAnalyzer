import pandas as pd
import numpy as np

def generate_data(n=150):
    print(" Generating realistic student data...")
    np.random.seed(42)
    data = {
        'Study_Hours': np.clip(np.random.normal(3.5, 1.5, n), 0, 10),
        'Sleep_Hours': np.clip(np.random.normal(6.5, 1.2, n), 4, 10),
        'Attendance': np.clip(np.random.normal(85, 10, n), 60, 100),
        'Previous_Marks': np.clip(np.random.normal(75, 15, n), 30, 100),
        'Subject': np.random.choice(['Math', 'Science', 'English'], n)
    }
    
    # Generate marks FIRST
    marks = (data['Study_Hours']*8 + data['Sleep_Hours']*5 + 
             data['Attendance']*0.3 + data['Previous_Marks']*0.4 + 20)
    data['Final_Marks'] = np.clip(np.random.normal(marks, 8), 0, 100)
    
    df = pd.DataFrame(data)
    df.to_csv('student_data.csv', index=False)
    print(" Data generated: student_data.csv")
    print(f" Dataset shape: {df.shape}")
    print(df.head())
    return df

if __name__ == "__main__":
    generate_data()
