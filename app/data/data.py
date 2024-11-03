import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir)

# Load the datasets
students_df = pd.read_csv(os.path.join(data_dir, 'students.csv'))
courses_df = pd.read_csv(os.path.join(data_dir, 'courses.csv'))
enrollments_df = pd.read_csv(os.path.join(data_dir, 'enrollments.csv'))
projects_df = pd.read_csv(os.path.join(data_dir, 'projects.csv'))
attendance_df = pd.read_csv(os.path.join(data_dir, 'attendance.csv'))