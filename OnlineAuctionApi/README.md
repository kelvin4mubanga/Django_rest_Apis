# Django Online Auction REST API Project

A powerful simple online auction RESTful API built with Django and Django REST Framework. Designed with scalability, clean code practices, and modularity in mind it will be extended in future to add more functionality.

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
cd OnlineAuctionApi

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

| GET    | /api/ | List all items on auction sale|
| POST   | /api/ | adds  an item to auction sale list|
| GET    | /api/<id>/ | Retrieve an item on the auction sals list|
| PUT    | /api/<id>/ | Update an item on the auction sales list|
| DELETE | /api/<id>/ | Delete item an item on the auction sales list|

| GET    | /api/AuctionCategory | List all auction categories|
| POST   | /api/ | adds  an item to the auction category list|
| GET    | /api/AuctionCategory/<id>/ | Retrieve an auction n category list|
| PUT    | /api/AuctionCategory/<id>/ | Update an auction category list |
| DELETE | /api/AuctionCategory/<id>/ | Delete an auction category list|

| GET    | /api/Bid| List all Bids on all items|
| POST   | /api/Bid/<id>/ | Retrieve a Bid on item |
| PUT    | /api/Bid/<id>/ | Update a Bid on item |
| DELETE | /api/Bid/<id>/ | Delete a Bid on item |


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


