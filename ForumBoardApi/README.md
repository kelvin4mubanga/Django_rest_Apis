# Django ForumBoardApi REST API Project

A powerful simple ForumBoardApi RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

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
cd ForumBoardApi

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
| GET    | /api/ForumThread | List all ForumThread |
| POST   | /api/ForumThread | Create a ForumThread|
| GET    | /api/ForumThread/<id>/ | Retrieves a ForumThread|
| PUT    | /api/ForumThread/<id>/ | Updates ForumThread|
| DELETE | /api/ForumThread/<id>/ | Deletes a ForumThread|
| GET    | /api/ForumPost | List all ForumPost |
| POST   | /api/ForumPost | Create a ForumPost|
| GET    | /api/ForumPost/<id>/ | Retrieves a ForumPost|
| PUT    | /api/ForumPost/<id>/ | Updates a ForumPost|
| DELETE | /api/ForumPost/<id>/ | Deletes a ForumPost|




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


