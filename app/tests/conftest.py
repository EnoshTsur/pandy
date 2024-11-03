import pytest

from app.data.data import students_df, courses_df, enrollments_df, projects_df, attendance_df

@pytest.fixture(scope="package")
def students():
    return students_df

@pytest.fixture(scope="package")
def courses():
    return courses_df

@pytest.fixture(scope="package")
def enrollments():
    return enrollments_df

@pytest.fixture(scope="package")
def projects():
    return projects_df

@pytest.fixture(scope="package")
def attendance():
    return attendance_df

