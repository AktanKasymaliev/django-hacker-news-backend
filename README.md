# simple hacker news backend

Hello, in the first, you sould clone rep:
* cloning repository:
```
git clone https://github.com/AktanKasymaliev/online_store.git
```
* Download virtual enviroment:
```
pip install python3-venv 
Activating: python3 -m venv venv
```
* Install all requirements: 
```
pip install -r requirements.txt
```

* Create a file .env on self project level, copy under text, and add your value: 
```
SECRET_KEY = 
DEBUG = 
DB_PASSWORD = 
DB_USER = 
DB_NAME = 
```

* This project working on Postgresql, so install him:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo -u postgres psql
```
* Enter in your postgresql, and create database:
```
sudo -u postgres psql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```

* Sync database with Django:
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```


* And finally start project: `python3 manage.py runserver`

#### Postman collection: https://web.postman.co/workspace/My-Workspace~a9d49b78-fa0f-4ace-86c5-5857e23a6310/documentation/14689518-81e713de-c6da-4a87-8622-42504c36fefc
#### Deployed project: https://boiling-river-68889.herokuapp.com/
