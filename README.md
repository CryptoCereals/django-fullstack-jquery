# django-fullstack-jquery
Django FullStack example with Jquery. 

## Apps included
A subapp is any app create after project creation:

| Parent App | App | Description |
| --- | --- | --- |
| - | django_login | Control before accessing platform |
| - | django_onepage | Django onepage with ajax(Jquery) |

## Bootstrap theme
We use admin-lte as base for the front-end part.
Check this website to know how it works:
https://adminlte.io/themes/v3/pages/UI/general.html

## Development
You only need to have the correct version of Python to start to develop.
We suggest doing it on a virtualenv.
### Requirements :
- Python 3.8
    - virtualenv 20.4.7

## Usage
Install python dependencies
```bash
pip install -r requirements-dev.txt
```
Modify private.ini for your environnement

First configurations steps and then create admin user
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Start Django
```bash
python manage.py runserver 0.0.0.0:8000
```

Create a new app.
First create directory in chosen path and then execute command.
IMPORTANT: Settings only detect apps in 'subapps' folder
```bash
python manage.py startapp basemaps subapps/login
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://raw.githubusercontent.com/CryptoCereals/django-fullstack-jquery/main/LICENSE)