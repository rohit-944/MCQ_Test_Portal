MCQ Test Portal
----------------

Overview:- 
The MCQ Test Portal is a web-based application developed for users to take multiple-choice questions (MCQ) tests. It offers features such as test creation, test-taking, result tracking, and an admin portal. The system uses Django as the backend framework with SQLite as the database, and it is designed to be lightweight and user-friendly.

Features:-
User Registration and Authentication
Test Creation (Admin)
MCQ Test Interface for Users
Storing and Retrieving Test Results
Analytics on Test Performance


Technologies Used
Backend
Python: Core programming language.
Django: A Python web framework used to build the backend logic and REST APIs.
SQLite: Lightweight database for storing user data, test questions, and results.
Frontend
HTML/CSS: For structuring and styling the web pages, providing a clean and responsive interface.
Setup Instructions
Prerequisites
Before you can run the project, make sure you have:

Python 3.x installed
pip (Python package manager)
A code editor (e.g., Visual Studio Code, PyCharm)
Steps to Run
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/MCQ_Test_Portal.git
cd MCQ_Test_Portal
Set Up a Virtual Environment (Optional) Create and activate a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies Install required dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Set Up the Database Run migrations to set up the SQLite database:

bash
Copy code
python manage.py migrate
Create a Superuser (Admin) Create an admin account to access the admin panel:

bash
Copy code
python manage.py createsuperuser
Run the Development Server Start the Django development server:

bash
Copy code
python manage.py runserver
Access the Application Open your web browser and navigate to http://localhost:8000 to view the MCQ Test Portal.

Admin Interface
Access the Django Admin Interface at http://localhost:8000/admin.
Log in with the superuser credentials created earlier.
You can add test questions, manage users, and view test results from this panel.
