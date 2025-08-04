# Django job listings  REST API Project

A powerful simple  job listings RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

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
cd JobListingsApi

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
| GET    | /api/Company | List all Companies |
| POST   | /api/Company | Create a Company|
| GET    | /api/Company/<id>/ | Retrieve a Company |
| PUT    | /api/Company/<id>/ | Update a Company |
| DELETE | /api/Company/<id>/ | Delete  a Company |

| GET    | /api/ | List all Jobs |
| GET    | /api/job/detail/<id>| list job details|
| GET    | /api/JobCategory/ | Retrieve all job category |
| GET    | /api/JobCategory/<id>/ | Retrieve a JobCategory |
| PUT    | /api/JobCategory/<id>/ | Update a JobCategory|
| DELETE | /api/JobCategory/<id>/ | Delete  a JobCategory |

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


