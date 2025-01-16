# Ezekiel Oluwadamilare jvec-assessment-backend

## This is the jvec assessment backend repository

## Run this  app with `python manage.py runserver`

## Getting Started
1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine:
   git clone <https://github.com/Damieee/jvec-assessment-backend.git>

3. Navigate to the project directory using Command Prompt or IDE Teminal:
    cd jvec-assessment-backend

4. Create a virtual environment (recommended):
    `python -m venv venv`

5. Activate the virtual environment:
    - On Windows:
    `venv\Scripts\activate`
    - On macOS and Linux:
    `source venv/bin/activate`

6. Install the required dependencies:
    `pip install -r requirements.txt`

7. Run the Django development server:
    `python manage.py runserver`

Your application should now be running at [http://localhost:8000/](http://localhost:8000/).


## API Endpoints

This backend application provides various API endpoints for different functionalities. Below are some of the primary endpoints:

- `POST /api/authentication/register/`: Register a new user.
- `POST /api/authentication/login/`: Log in with an existing user.
- `POST /api/authentication/logout/`: Log out an existing user.
- `POST /api/contacts/create/`: Create a new contact for the authenticated user.
- `GET /api/contacts/list/`: List all contacts for the authenticated user.
- `GET /api/contacts/retrieve/<contact_id>/`: Retrieve a specific contact.
- `PUT /api/contacts/update/<contact_id>/`: Update a specific contact.
- `DELETE /api/contacts/delete/<contact_id>/`: Delete a specific contact.
- `GET /swagger`: Get the Swagger Documentation of this application backend for easy readability and Maintainability.

Please make sure to authenticate your requests using the appropriate authentication methods (e.g., JWT token-based authentication) when accessing protected endpoints.

## API LINK

jvec-backend-solution.onrender.com

## Dependies

- pip==23.3.1
- Django
- djangorestframework==3.14.0
- djangorestframework_simplejwt==5.3.0
- drf_yasg==1.21.7
- email_validator==2.0.0.post2
- gunicorn

