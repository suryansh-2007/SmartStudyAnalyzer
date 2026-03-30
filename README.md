# Smart Study Pattern Analyzer

A machine learning project that analyzes student study patterns and predicts academic performance based on realistic data. This tool is designed for educational insights, live predictions, and professional data visualization.

## Features

- **Synthetic Data Generation:** Automatically creates a realistic dataset of student study habits, sleep hours, attendance, previous marks, and subjects.
- **ML Model Training:** Trains a Random Forest regression model to predict final marks using the generated data.
- **Insightful Analytics:** Generates key insights and professional graphs, including study hours vs. marks, subject performance, and marks distribution.
- **Live Prediction Demo:** Instantly predicts student marks for custom input scenarios, highlighting risk levels (pass/fail).
- **Easy Submission:** All outputs (dataset, model, graphs, predictions) are generated and ready for project submission.

## How It Works

1. **Data Generation:**  
	Generates a dataset (`student_data.csv`) with realistic student records.

2. **Model Training:**  
	Trains a machine learning model (`study_model.pkl`) to predict final marks based on study patterns.

3. **Insights & Visualization:**  
	Analyzes the data and creates insightful graphs (`insights.png`).

4. **Live Prediction:**  
	Provides a demo for predicting marks based on user input.

## Usage

1. Install dependencies:
	```
	pip install -r requirements.txt
	```

2. Run the main script:
	```
	python main.py
	```

3. Outputs:
	- `student_data.csv` — Generated dataset
	- `study_model.pkl` — Trained ML model
	- `insights.png` — Analytical graphs
	- Console — Live prediction demo

## File Overview

- `data_generator.py` — Generates synthetic student data.
- `model_trainer.py` — Trains and saves the ML model.
- `insights.py` — Produces insights and graphs.
- `predictor.py` — Predicts marks for new student data.
- `main.py` — Orchestrates the full workflow.
- `requirements.txt` — Python dependencies.

