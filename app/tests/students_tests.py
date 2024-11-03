import pandas as pd


# Exercise 1: Find all Python programmers
def test_find_python_programmers(students):
    python_devs = students[students['Favorite_Language'] == 'Python']

    # Assert the number of Python developers
    assert len(python_devs) == 6

    # Assert the specific students
    assert set(python_devs['Name'].values) == {
        'David HaMagid',
        'Yair Weissman',
        'Mordechai Oren',
        'Elkana Kalman',
        'Menachem Amrami',
        'Israel Vershaviak'
    }

    # Assert their frameworks
    assert set(python_devs['Favorite_Framework'].values) == {
        'Django', 'Flask', 'FastAPI', 'PyTorch', 'NumPy', 'TensorFlow'
    }

    # Assert their Student IDs
    assert set(python_devs['Student_ID'].values) == {
        'ST001', 'ST004', 'ST010', 'ST015', 'ST020', 'ST024'
    }


# Exercise 2: Count students by favorite programming language
def test_count_students_by_language(students):
    lang_counts = students['Favorite_Language'].value_counts()

    # Assert specific language counts
    assert lang_counts['Python'] == 6
    assert lang_counts['JavaScript'] == 5
    assert lang_counts['Java'] == 3
    assert lang_counts['Ruby'] == 2
    assert lang_counts['Go'] == 2

    # Assert total number of students
    assert len(students) == 25

    # Assert all unique languages
    expected_languages = {
        'Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go',
        'TypeScript', 'Rust', 'PHP', 'C++', 'Swift', 'Kotlin'
    }
    assert set(lang_counts.index) == expected_languages


# Exercise 3: Calculate average age by enrollment year
def test_average_age_by_enrollment(students):
    avg_age = students.groupby('Enrollment_Year')['Age'].mean()

    """
    students.groupby('Enrollment_Year') creates groups like this:

    2020 Group:
        Yehuda Zeev,23,Java,Spring Boot,ST003,2020,3.7
        Menachem Mendel Achrak,24,C#,.NET Core,ST005,2020,3.9
        Pinchas Waxberger,24,Java,Hibernate,ST011,2020,3.8
        Jonathan Rosenthal,24,C++,Qt,ST016,2020,3.7
        Menachem Mendel Ben Chaim,24,Go,Echo,ST022,2020,3.8

    2021 Group:
        David HaMagid,22,Python,Django,ST001,2021,3.8
        Reuven Cohen,21,JavaScript,React,ST002,2021,3.9
        ...

    2022 Group:
        students from 2022...

    2023 Group:
        students from 2023...
    """

    """
     students.groupby('Enrollment_Year')['Age']
     Now we just have the ages grouped by year:

     2020 Group: [23, 24, 24, 24, 24]
     2021 Group: [22, 21, 22, 23, 23, 22, 21, 22, 22, 23]
     2022 Group: [20, 21, 20, 21, 20, 21, 20, 21]
     2023 Group: [19, 19]
     """

    """
       students.groupby('Enrollment_Year')['Age'].mean()
       Enrollment_Year
       2020    23.8  # (23 + 24 + 24 + 24 + 24) / 5
       2021    22.1  # (22 + 21 + 22 + 23 + 23 + 22 + 21 + 22 + 22 + 23) / 10
       2022    20.5  # (20 + 21 + 20 + 21 + 20 + 21 + 20 + 21) / 8
       2023    19.0  # (19 + 19) / 2
       Name: Age, dtype: float64
       """

    # Assert we have all enrollment years
    assert set(avg_age.index) == {2020, 2021, 2022, 2023}

    # Count students per year
    year_counts = students['Enrollment_Year'].value_counts()
    assert year_counts[2021] == 10  # Most students enrolled in 2021
    assert year_counts[2022] == 8
    assert year_counts[2020] == 5
    assert year_counts[2023] == 2


# Exercise 4: Analyze GPA distribution
def test_gpa_analysis(students):
    # GPA stats
    assert students['GPA'].max() == 3.9
    assert students['GPA'].min() == 3.5
    assert 3.7 <= students['GPA'].mean() <= 3.8

    # Count high performers (GPA >= 3.8)
    high_performers = students[students['GPA'] >= 3.8]
    assert len(high_performers) == 10


# Exercise 5: Analyze framework popularity
def test_framework_analysis(students):
    framework_counts = students['Favorite_Framework'].value_counts()

    # Check specific frameworks
    spring_frameworks = students[
        students['Favorite_Framework'].str.contains('Spring')
    ]
    assert len(spring_frameworks) == 2  # Spring Boot and Spring

    js_frameworks = students[
        students['Favorite_Framework'].str.contains('js|JS|React|Vue|Svelte|Express')
    ]
    assert len(js_frameworks) == 5  # All JavaScript frameworks

    # Framework categories
    ml_frameworks = students[
        students['Favorite_Framework'].str.contains('PyTorch|TensorFlow|NumPy')
    ]
    assert len(ml_frameworks) == 3


# Exercise 6: Age distribution analysis
def test_age_distribution(students):
    age_stats = students['Age'].describe()
    print(age_stats)

    assert age_stats['min'] == 19
    assert age_stats['max'] == 24
    assert 21 <= age_stats['mean'] <= 22


# Exercise 7: Student ID format validation
def test_student_id_validation(students):
    student_ids = students['Student_ID']

    # Format validation
    assert all(s_id.startswith('ST') for s_id in student_ids)
    assert all(s_id[2:].isdigit() for s_id in student_ids)
    assert all(len(s_id) == 5 for s_id in student_ids)

    # Sequential validation
    id_numbers = [int(s_id[2:]) for s_id in student_ids]
    assert min(id_numbers) == 1
    assert max(id_numbers) == 25
    assert len(set(id_numbers)) == 25  # All unique


# Exercise 8: Programming language trends by year
def test_language_trends_by_year(students):
    pivot = pd.pivot_table(
        students,  # DataFrame we're using
        index='Enrollment_Year',  # Rows will be years
        columns='Favorite_Language',  # Columns will be languages
        aggfunc='size',  # Count occurrences
        fill_value=0  # Replace NaN with 0
    )

    # Check Python popularity across years
    assert pivot.loc[2021, 'C#'] == 0  # C# users in 2021
    assert pivot.loc[2022, 'Ruby'] == 1  # Ruby users in 2022

    # Check JavaScript distribution
    assert pivot.loc[2021, 'Rust'] == 1  # Rust users in 2021


# Exercise 9: Framework usage patterns
def test_framework_patterns(students):
    # Web frameworks vs Other frameworks
    web_frameworks = students[
        students['Favorite_Framework'].str.contains(
            'Django|React|Flask|Express|Next.js|Vue|Laravel|Svelte'
        )
    ]
    assert len(web_frameworks) >= 7  # At least 10 web frameworks

    # Framework diversity
    framework_counts = students['Favorite_Framework'].nunique()
    assert framework_counts >= 20  # At least 20 different frameworks
