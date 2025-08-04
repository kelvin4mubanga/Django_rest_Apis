# Django Property Rentals REST API Project

A powerful simple Property Rentals RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

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
cd PropertyRentalApi

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
| GET    | /api/ | List all properties for rent|
| POST   | /api/ | Create a properties for rent  |
| GET    | /api/<id>/ | Retrieve a properties for rent |
| PUT    | /api/<id>/ | Update a properties for rent |
| DELETE | /api/<id>/ | Delete a properties for rent |




| GET    | /api/PropertyCategory | List all property category|
| POST   | /api/PropertyCategory| Create a property category|
| GET    | /api/PropertyCategory/<id>/ | Retrieve a property category |
| PUT    | /api/PropertyCategory/<id>/ | Update a property category|
| DELETE | /api/PropertyCategory/<id>/ | Delete a property category |



| GET    | /api/Booking | List all Booking  |
| POST   | /api/Booking | Create a Booking on a property |
| GET    | /api/Booking/<id>/ | Retrieve a Booking on property |
| PUT    | /api/Booking/<id>/ | Update a book Booking on property|
| DELETE | /api/Booking/<id>/ | Delete a bokki Booking on property|

| GET    | /api/Review | List all reviews |
| POST   | /api/Review | Create a review |
| GET    | /api/Review/<id>/ | Retrieve a review |
| PUT    | /api/Review/<id>/ | Update a review |
| DELETE | /api/Review/<id>/ | Delete a review |


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


