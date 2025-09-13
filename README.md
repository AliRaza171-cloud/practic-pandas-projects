Student Performance Data Analysis
Project Overview

This project analyzes student performance data using Python (Pandas).
The dataset contains student scores in Math, English, and Science, along with their Grade and Gender.

The project includes:

Descriptive statistics (mean, median, mode, std, min, max)

Top students per subject

Failing students list (marks < 50)

Pass/Fail percentage by Grade & Gender

Correlation analysis between Math & Science

 Exported results as CSV reports

Technologies Used

Python 3.x

Pandas (data manipulation & analysis)

CSV (input/output format)

Features & Analysis

General Statistics

Count of students

Students per Grade

Gender distribution per Grade

Subject-wise Analysis

Average, Median, Mode, Standard Deviation of scores

Top scorer in each subject

Failing students in each subject

Pass/Fail Percentages

Pass percentage by Grade

Fail percentage by Grade

Pass percentage by Gender

Fail percentage by Gender

Extra Insights

Correlation between Math and Science

Derived total score column for ranking students

Average score per Grade and per Gender

CSV Outputs

top_students.csv → Subject-wise toppers

failing_students.csv → Students scoring < 50

Avg_bt_grade.csv → Average subject scores by Grade

Avg_bt_gender.csv → Average subject scores by Gender

How to Run

Clone the repository:

git clone https://github.com/yourusername/student-performance-analysis.git
cd student-performance-analysis


Install requirements (if needed):

pip install pandas


Place your dataset file:

Put students_performance.csv in the project folder.

Run the script:

python student_data.py


Output CSV files will be saved in your Desktop (or the path you set in to_csv).

Example Outputs
Top Student Example
Subject: Math_Score
StudentID: 101
Name: Ali
Score: 98

Failing Student Example
StudentID: 105
Name: Sara
Subject: English_Score
Score: 35

Pass Percentage Example
9th in 85.71%
10th in 92.30%

Example:

 Learning Outcomes

Mastered data manipulation with Pandas

Learned groupby, filtering, aggregation

Practiced real-world data cleaning & reporting

Exported structured CSV reports for further use

 Next Steps

Learn NumPy for numerical computing

Start with Machine Learning models (scikit-learn)

Build real-world ML projects (classification, regression, prediction models)

Author

Ali Raza

📌 Connect with me on LinkedIn

💻 GitHub: AliRaza171
