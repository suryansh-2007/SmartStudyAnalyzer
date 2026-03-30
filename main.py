
"""
 SMART STUDY PATTERN ANALYZER - COLLEGE PROJECT
Run: python main.py
"""

print(" Smart Study Pattern Analyzer")
print("=" * 50)

# RUN ALL MODULES
from data_generator import generate_data
from model_trainer import train_model
from insights import generate_insights
from predictor import predict_marks

print(" Generating Student Data...")
generate_data()

print(" Training ML Model...")
accuracy = train_model()
print(f"  Model Accuracy: {accuracy:.3f}")

print(" Generating Insights & Graphs...")
generate_insights()

print("\n LIVE PREDICTION DEMO:")
print("   (Real student predictions)")
predict_marks(1.5, 8.0, 70, 55, 'Math')      # Lazy student
predict_marks(4.0, 7.0, 90, 80, 'Science')  # Average student  
predict_marks(6.0, 6.5, 95, 90, 'English')  # Top student

print("\n" + "=" * 50)
print(" PROJECT COMPLETE - READY FOR SUBMISSION!")
print(" OUTPUT FILES:")
print("   • student_data.csv    (Dataset)")
print("   • study_model.pkl     (ML Model)")
print("   • insights.png        (Graphs)")
print("   • Console predictions (Demo)")
print("\n🎓 Submit this folder as-is!")