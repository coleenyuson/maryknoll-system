##### A Software Engineering 2 project:
## Maryknoll Academy of Cateel Enrollment System

A software engineering 2 project: Enrollment System for Maryknoll Academy of Cateel

## Getting Started

To get yourself a copy of the project up and running on your local machine for development and testing purposes:

1.) Create your workspace folder and open your command line to your workspace folder

2.) Register the repository link (https://github.com/aaajii/sad-development.git) to a remote 

``` git remote add origin https://github.com/aaajii/sad-development.git ```

3.) Clone the repository to your folder to make yourself have your own local copy of it

``` git clone origin ```

### Prerequisites

The project strictly requires the latest version of python 2 (or 3) and Django1.9 .

Assuming you are using any linux OS (or git bash on windows), you can run this in your command line:
```
sudo apt-get update
sudo apt-get install python-pip
sudo pip install django==1.9
```

To check if you have successfully installed django and its version:
```
django-admin --version
```

lastly, this project uses django-widget-tweaks. To install this:

```
sudo pip install django-widget-tweaks
```

## Running the tests

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver

## Built With

* [Django 1.9](https://docs.djangoproject.com/en/2.0/releases/1.9/) - The web framework used

## Deployment

Configure the web host's WSGI with:

```
import os
import sys

#assuming your manage.py is located at /home/user/lol-project then
path = '/home/user/lol-project'
if path not in sys.path:
    sys.path.append(path)

#assuming your settings.py is located at /home/user/lol-project/lol-project then
os.environ['DJANGO_SETTINGS_MODULE'] = 'local_library_website.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

import necessary virtual environments first if needed!

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* chynna

