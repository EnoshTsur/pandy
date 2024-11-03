import pandas as pd

def test_add_student(students):
    """Add a new student to the DataFrame"""
    student_to_add = {
        'Name': 'Moshe Levi',
        'Age': 21,
        'Favorite_Language': 'Python',
        'Favorite_Framework': 'Django',
        'Student_ID': 'ST026',
        'Enrollment_Year': 2023,
        'GPA': 3.7
    }
    new_students = pd.concat([
        students,
        pd.DataFrame([student_to_add])
    ], ignore_index=True)
    assert 'Moshe Levi' in new_students['Name'].values

def test_add_multiple_students(students):
    """Add multiple students at once"""
    students_to_add = [
        {
            'Name': 'Yosef Cohen',
            'Age': 20,
            'Favorite_Language': 'JavaScript',
            'Favorite_Framework': 'React',
            'Student_ID': 'ST027',
            'Enrollment_Year': 2023,
            'GPA': 3.6
        },
        {
            'Name': 'David Miller',
            'Age': 22,
            'Favorite_Language': 'Python',
            'Favorite_Framework': 'Flask',
            'Student_ID': 'ST028',
            'Enrollment_Year': 2023,
            'GPA': 3.8
        }
    ]
    new_students = pd.concat([
        students,
        pd.DataFrame(students_to_add)
    ], ignore_index=True)

    assert all(
        name in new_students['Name'].values
        for name in ['Yosef Cohen', 'David Miller']
    )

def test_create_derived_column(students):
    """Create a new column 'Age_Group' based on Age"""
    students_copy = students.copy()
    students_copy['Age_Group'] = students_copy['Age'].apply(lambda age:
        'Young' if age < 21 else
        ('Mid' if age < 23 else 'Senior'))

    assert all(
        age_group in students_copy['Age_Group'].values
        for age_group in ['Young', 'Mid', 'Senior']
    )

def test_create_language_category(students):
    """Create a column categorizing languages as 'Compiled' or 'Interpreted'"""
    students_copy = students.copy()
    compiled_langs = {'Java', 'C#', 'C++', 'Rust', 'Swift', 'Go', 'Kotlin'}
    students_copy['Language_Type'] = students_copy['Favorite_Language'].apply(
        lambda fav_language: 'Compiled' if fav_language in compiled_langs
        else 'Interpreted'
    )
    assert all(
        lan_type in students_copy['Language_Type'].values
        for lan_type in ['Compiled', 'Interpreted']
    )

def test_create_student_email(students):
    """Create email addresses for students based on their names"""
    students_copy = students.copy()
    students_copy['Email'] = students_copy['Name'].apply(
        lambda name: f"{name.lower().replace(' ', '.')}@university.com"
    )
    assert all(
        '@university.com' in email
        for email in students_copy['Email'].values
    )

def test_filter_high_performers(students):
    """Get all students with GPA > 3.8"""
    high_performance = students[students['GPA'] > 3.8]
    assert all(gpa > 3.8 for gpa in high_performance['GPA'].values)

def test_find_language_users(students):
    """Find all Python and JavaScript users"""
    py_and_js = students[
        students['Favorite_Language'].isin(['Python', 'JavaScript'])
    ]
    assert all(
        lan in py_and_js['Favorite_Language'].values
        for lan in ['Python', 'JavaScript']
    )

def test_complex_query(students):
    """Find young students (age < 22) with high GPA (> 3.7) enrolled after 2021"""
    complex_query = students[
        (students['Age'] < 22) &
        (students['GPA'] > 3.7) &
        (students['Enrollment_Year'] > 2021)
    ]

    assert all(age < 22 for age in complex_query['Age'].values)
    assert all(gpa > 3.7 for gpa in complex_query['GPA'].values)
    assert all(
        enrollment > 2021
        for enrollment in complex_query['Enrollment_Year'].values
    )

def test_group_and_average(students):
    """Calculate average GPA by favorite programming language"""
    avg_gpa_by_language = students.groupby('Favorite_Language')['GPA'].mean()
    assert avg_gpa_by_language.idxmax() == 'C#'
    assert avg_gpa_by_language.idxmin() == 'Swift'

def test_update_gpa(students):
    """Increase GPA by 0.1 for all students enrolled in 2023"""
    # 1. loc: Label-based access (uses index labels/column names)
    # Syntax: df.loc[row_label, column_label]
    df = students.copy()
    df.loc[df['Enrollment_Year'] == 2023, 'GPA'] += 0.1
    assert all(
        gpa > 0.1
        for gpa in df.loc[df['Enrollment_Year'] == 2023, 'GPA'].values
    )

def test_language_indexing(students):
    languages = students.iloc[0:3, 2]
    assert all(
        lan in ['Python', 'JavaScript', 'Java']
        for lan in languages
    )


