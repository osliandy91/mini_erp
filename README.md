# MINI ERP - Project Management

This is a basic ERP system for project management, developed with **Django** as the backend API using **Django Rest Framework**.

## Features
- Create, Update, List, Get and Delete projects
- REST API with Django Rest Framework

## Technologies Used
- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL (optional)

## Installation
1. Clone the repository:
```sh
   git clone https://github.com/your-username/erp-projects.git
   cd erp-projects
```

2. Create and activate a virtual environment:
```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```sh
   pip install -r requirements.txt
```

4. Configure the database in `settings.py`.

5. Apply migrations:
```sh
   python manage.py migrate
```

6. Run the server:
 ```sh
   python manage.py runserver
```

## Usage
You can test the API using tools like **Postman** or **cURL**, by sending requests to `http://localhost:8000/api/projects/`.


## Admin
You can create a superuser for the admin area
```sh
 python manage.py createsuperuser
 ```
 Then you can access `http://127.0.0.1:8000/admin/`

## Contribution
If you want to contribute, submit a pull request or open an issue.

## License
This project is licensed under the MIT License.
