# Django E-Learning REST API Project

A powerful simple Blockchain RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

## 🚀 Features

- RESTful API architecture
- Token-based authentication (JWT or TokenAuth)
- CRUD functionality
- Unit & integration tests
- SQLite support
- 

## 🔧 Tech Stack

- Python 3.9 and above
- Django 5.0
- Django REST Framework
- SQLite 
-unittest

## 📦 Installation

```bash
git clone https://github.com/kelvin4mubanga/Django_apis.git
cd ElearnigApi

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
```

# creating a superuser

```bash
 python manage.py createsuperuser
  #Enter your desired username and press enter.
  #e.g
Username: admin
password:admin123


```


## ⚙️ Running the Server

```bash
python manage.py runserver
```





## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/Course | List all Course |
| POST   | /api/Course | Create a Course|
| GET    | /api/Course/<id>/ | Retrieve a Course |
| PUT    | /api/Course/<id>/ | Updates a Course |
| DELETE | /api/Course/<id>/ | Deletes a Course |
| GET    | /api/Enrollment | List all Enrollments |
| POST   | /api/Enrollment| Create a Enrollment|
| GET    | /api/Enrollment/<id>/ | Retrieve a Enrollment |
| PUT    | /api/Enrollment/<id>/ | Updates an Enrollment |
| DELETE | /api/Course/<id>/ | Deletes an Enrollment |
| GET    | /admin/ | admin login |


## 🧪 Running Tests

```bash
python manage.py test
```



## 📄 License

MIT License

## 👤 Author

Kelvin Mubanga  
Email: kelvinmunanga045@.com  
GitHub: [github.com/kelvinm4ubanga](https://github.com/kelvin4mubanga)


