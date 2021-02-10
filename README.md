# Photo Album app

Photo Album application. Users can upload their images.

Key Features:
* Registration/Login. 
* Ability of CRUD operations of photos for each user.

# Technologies
* django==3.1.6
* djangorestframework==3.12.2


## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
```
1) virtualenv venv
2) source venv/bin/activate
3) pip install -r requirements.txt
```
Setup Env Variables. Create .env file along-side manage.py module

|    NAME   |                      DESCRIPTION                      |DEFAULT VALUE|
|-----------|-------------------------------------------------------|-------------|
|DEBUG      |Debug mode for local machine, set `False` on porduction|     False    |
|SECRET_KEY |Secret key for encrypting password and etc secure value|  - |
|DATABASE_URL |Your DB url Ex: `sqlite:////tmp/sqlite3.db`| - |
|ALLOWED_HOSTS | A list of strings representing the host/domain names that this Django site can serve. | - |

```
5) python manage.py migrate 
6) python manage.py loaddata fixtures/data.json  #loading to db existing data
7) python manage.py runserver 
```


## Authors

* **Almaz Yusupov** - [Almaz97](https://github.com/Almaz97)


## Other Info

* API documentation can be reached by `/swagger/` endpoint
* Pushing media folder to repository is not a good practice! I'm adding 
media, because of interview task and to avoid the image urls to be broken after loading data
* Due to lack of time I didn't manage to cover task points related to user notifications
