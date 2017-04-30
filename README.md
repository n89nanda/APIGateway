API Gateway
============

Description
-------------
This is a starter template to deploy REST Endpoints as fast and easy as possible. This project uses [Flask](http://flask.pocoo.org/) microframework and can be deployed on [Heroku](https://www.heroku.com/). 




TL;DR
----------------------
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Deploy to Heroku. No configuration necessary, just press the above magic button! 

Getting started
------------
### Clone this repo on your local machine using Git
    $ mkdir APIGateway
    $ cd APIGateway
    $ git init
    $ git clone https://github.com/n89nanda/APIGateway.git
    $ cd APIGateway
    $ source APIGateway/bin/activate

### Installing packages
    $ pip install -r requirements.txt

### Running the application server locally
    $ python app.py

### Using cURL to test the server endpoint 
    $ curl http://localhost:5000/

Sample ToDo Application
------------
This project implements a basic ToDo list application. 
Refer `backend.py` that stores all the tasks and valid users. Refer `app.py` that contains the API endpoint definitions 

Using API endpoints, this app can implement the following functions
### Add a task 
Using HTTP POST, we add a task. The task is in a json format

    $ curl http://localhost:5000/todo/api/v1.0/tasks -X POST -d '{"title":"my first task"}' -H "Content-type: application/json"
    
### Retrieve all tasks
Using HTTP GET along with Basic authentication, retrieve all tasks.

    $  curl http://localhost:5000/todo/api/v1.0/tasks -u Alice:password
    
### Retrieve a specific task
Using  HTTP GET along with task ID, retrieve a specific task

    $ curl http://localhost:5000/todo/api/v1.0/tasks/1
    
### Update a specific task
Using  HTTP PUT along with task ID, update a specific task

    $ curl http://localhost:5000/todo/api/v1.0/tasks/1 -X PUT -d '{"done":true}' -H "Content-Type: application/json"
    
### Delete a specific task 
Using  HTTP DELETE along with task ID, delete a specific task

    $ curl http://localhost:5000/todo/api/v1.0/tasks/1 -X DELETE


Deploying on Heroku using Git
------------

If you haven't [signed up for Heroku](https://api.heroku.com/signup), go ahead and do that. Follow the below commands after [installing the Heroku toolkit CLI](https://toolbelt.heroku.com/) 

Note: You need to be in the root directory of the application that contains `requirements.txt` and `Procfile` before you push to Heroku.

    $ heroku login
    $ heroku create
    $ git push heroku master
    $ heroku ps:scale web=1
    $ heroku open
    
