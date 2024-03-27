# Test Case Manager

Test Case Manager is a web application developed using Postgres, Django, jQuery, and Sass. It provides functionality for managing test cases, including creating, editing, organizing, test cases as part of software testing processes.

## Features

- **Test Case Creation**: Create new test cases with detailed descriptions, steps, expected results, and other relevant information.
- **Test Case Organization**: Organize test cases into categories, projects, or other custom structures for better Manager and navigation.
- **User Authentication**: Secure user authentication and authorization to ensure that only authorized users can access and modify test cases.
- **Reporting**: Generate reports on test case execution status, trends, and other metrics to track testing progress and identify areas for improvement.

## Technologies Used

- PostgreSQL
- Django
- jQuery
- Sass

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/test-case-Manager.git
   ```

2. Navigate to the project directory:
   ```bash
   cd test-case-Manager
   ```

3. Set up the PostgreSQL database:
   - Create a new PostgreSQL database for the application.
   - Configure the database settings in the Django settings file (`settings.py`).

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Log in to the application using your credentials.
2. Explore the dashboard and navigation menu to access different features and functionalities.
3. Create new test cases, organize them into categories or projects.
4. Use the reporting features to track testing progress, analyze test results, and generate insights for improvement.
