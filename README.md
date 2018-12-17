# BreazeHome Capstone Project (RickRoda)
SECRET_KEY has been removed. __THIS PROJECT WILL NOT COMPILE WITHOUT THE SECRET_KEY.__
This is purely on GitHub to showcase my programming skills to potential employers.
Send me a message if you would like to discuss my contributions to this project.

# Breaze - API
Django REST Framework For Breaze API

## Installing

__Locally__

First install python3+ on your machine and then download and install [pip][1].
Then from the root of the project run:

1. `python3.5 -m venv venv` - Create a virtual environment in the venv folder
2. `source venv/bin/activate` - Load the environment
  - On Windows: `venv/Scripts/activate.bat`
3. `pip install -r requirements.txt` - Install dependencies

To run the the server use the following commands:

1. `python manage.py migrate`
2. `python manage.py runserver`

To run the server in development ensure you have `DEBUG` and `DB_DEBUG` set to
True in your environment.

You can provide a port after the `runserver`. However, the default is 8000.


__Using Docker__

This project can also be ran using docker. Docker is a container system meant
to run an application with the same environment it was built in. This ensures
dependencies remain the same on every system. To get started, install the
docker toolbox with your favorite package manager. On mac, run  `brew cask
install dockertoolbox` to get the tools that you'll need.

For every other system, vist [docker's website][3] for installation
istructions.

To run this using docker, make sure that your docker machine is running if you
are on Mac/Windows. To create a virtualbox using `docker-machine` and then load
it use the following commands:

1. `docker-machine create --driver virtualbox default`
2. `docker-machine start default`
3. `eval $(docker-machine env default)`

Once the previous commands are done you should have a working VM running and
loaded. Use `docker ps` to get a list of docker containers (should be empty at
this time).

Finally, to start the app:
`cd $API_DIR && docker-compose up -d --build`


## Introduction

Breaze-api stores and manages the backend components to the [Breaze app][4]


## Authentication

Our API uses [token authentication][5].

For clients to authenticate, the token key should be included in the
Authorization HTTP header. The key should be prefixed by the string literal
"Token", with whitespace separating the two strings. For example:

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

__OAuth__

A good oveview of oauth2 can be found [here][6].

To use OAuth authentication you must first be sure to add the each client ID and
key to the app you would like to use in the admin panel at:

`/admin/socialaccount/socialapp/` Note: Ensure the sites are also added.




### Dependencies

* Django
* django-rest-swagger
* djangorestframework
* Markdown
* PyYAML
* ... see more in requirements.txt

These are installed when the `pip install` command is ran.

[1]: https://pip.pypa.io/en/latest/installing/
[2]: https://docs.python.org/3/using/scripts.html
[3]: https://docs.docker.com/engine/installation/
[4]: http://www.breazehome.com
[5]: http://www.django-rest-framework.org/api-guide/authentication/
[6]: https://developers.google.com/identity/sign-in/web/server-side-flow
