# Django Travel REST API Project

A powerful simple Travel RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

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
cd TravelApi
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
| GET    | /api/ | List all destination |
| POST   | /api/ | Create a destination |
| GET    | /api/<id>/ | Retrieve a destination|
| PUT    | /api/<id>/ | Update a destination|
| DELETE | /api/<id>/ | Delete a destination|

| GET    | /api/TravelPackage | List all Travel Package|
| POST   | /api/TravelPackage | Create a Travel Package |
| GET    | /api/TravelPackage/<id>/ | Retrieve a Travel Package |
| PUT    | /api/TravelPackage/<id>/ | Update a Travel Package |
| DELETE | /api/TravelPackage/<id>/ | Delete Travel Package |

| GET    | /api/Booking | List all Booking|
| POST   | /api/Booking | Create a Booking |
| GET    | /api/Booking/<id>/ | Retrieve Booking |
| PUT    | /api/Booking/<id>/ | Update Booking |
| DELETE | /api/Booking/<id>/ | Delete Booking|

| GET    | /api/Review | List all reviews|
| POST   | /api/Review | Create a review|
| GET    | /api/Review/<id>/ | Retrieve a review|
| PUT    | /api/Review/<id>/ | Update a review |
| DELETE | /api/Review/<id>/ | Delete a review|


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


