import pandas as pd

# Exercise 1: Find all courses taught by Dr. Enosh Tsur
def test_find_enosh(courses):
    by_enosh = courses[courses['Instructor'] == 'Dr. Enosh Tsur']
    # Assert the number of courses he teaches
    assert len(by_enosh) == 2

    # Assert the specific courses he teaches
    assert (set(by_enosh['Course_Name'].values) ==
            {'Database Systems', 'Data Science Fundamentals'})

    # Assert the departments he teaches in
    assert (set(by_enosh['Department'].values) ==
            {'Computer Science', 'Data Science'})

    # Assert course IDs
    assert (set(by_enosh['Course_ID'].values) ==
            {'CS301', 'DS101'})

    # Assert all rows have the correct instructor
    assert all(
        instructor == 'Dr. Enosh Tsur'
        for instructor in by_enosh['Instructor']
    )

    # Assert the difficulty levels of his courses
    assert set(by_enosh['Difficulty_Level'].values) == {'Intermediate', 'Beginner'}

    # Assert the credits of his courses
    assert all(credit == 3 for credit in by_enosh['Credits'])


# Exercise 2: Count how many courses are there per department
def test_count_courses_per_department(courses):
    dept_counts = courses['Department'].value_counts()

    # Assert total number of courses
    assert len(courses) == 10

    # Assert specific department counts
    assert dept_counts['Computer Science'] == 5
    assert dept_counts['Web Development'] == 3
    assert dept_counts['Data Science'] == 2

    # Assert these are all the departments
    assert set(dept_counts.index) == {'Computer Science', 'Web Development', 'Data Science'}

# Exercise 3: Calculate average credits for each difficulty level
def test_average_credits_by_difficulty(courses):
    # The original data might look like this:
    """
    Difficulty_Level    Credits
    Beginner           3
    Beginner           3
    Beginner           3
    Intermediate       3
    Intermediate       4
    Intermediate       3
    Advanced           4
    Advanced           4
    """

    # After groupby('Difficulty_Level'), you have three groups:
    """
    Beginner group: [3, 3, 3]
    Intermediate group: [3, 4, 3]
    Advanced group: [4, 4]
    """

    # After .mean(), you get:
    """
    Difficulty_Level
    Beginner       3.0
    Intermediate   3.5
    Advanced       4.0
    """
    avg_credits = courses.groupby('Difficulty_Level')['Credits'].mean()
    print(avg_credits)

    # Assert average credits for each level
    assert avg_credits['Beginner'] == 3.0
    assert avg_credits['Intermediate'] == 3.5
    assert avg_credits['Advanced'] == 4.0

    # Assert we have all difficulty levels
    assert set(avg_credits.index) == {'Beginner', 'Intermediate', 'Advanced'}


# Exercise 4: Find and sort beginner courses
def test_sorted_beginner_courses(courses):
    beginner_courses = courses[
        courses['Difficulty_Level'] == 'Beginner'
        ].sort_values('Course_Name')


    # Assert number of beginner courses
    assert len(beginner_courses) == 3

    # Assert course names are in correct order
    assert list(beginner_courses['Course_Name']) == [
        'Data Science Fundamentals',
        'Introduction to Programming',
        'Web Development Basics'
    ]

    # Assert all are actually beginner courses
    assert all(
        level == 'Beginner'
        for level in beginner_courses['Difficulty_Level']
    )

# Exercise 5: Test pivot table of department and difficulty
def test_difficulty_by_department(courses):
    pivot = pd.pivot_table(
        courses,  # DataFrame to pivot
        index='Department',  # Rows
        columns='Difficulty_Level',  # Columns
        aggfunc='size',  # What to calculate (here: count)
        fill_value=0  # Replace NaN with 0
    )

    print(pivot)

    # Assert Computer Science department counts
    assert pivot.loc['Computer Science', 'Beginner'] == 1
    assert pivot.loc['Computer Science', 'Intermediate'] == 2
    assert pivot.loc['Computer Science', 'Advanced'] == 2

    # Assert Web Development department counts
    assert pivot.loc['Web Development', 'Beginner'] == 1
    assert pivot.loc['Web Development', 'Intermediate'] == 1
    assert pivot.loc['Web Development', 'Advanced'] == 1

    # Assert Data Science department counts
    assert pivot.loc['Data Science', 'Beginner'] == 1
    assert pivot.loc['Data Science', 'Intermediate'] == 1
    assert pivot.loc['Data Science', 'Advanced'] == 0


def test_course_full_name(courses):
    courses['Full_Name'] = courses.apply(
        lambda row: f"{row['Course_ID']}: {row['Course_Name']}",
        axis=1
    )