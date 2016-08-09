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
    

    





First, you'll need to clone the repo.

    $ git clone git@github.com:zachwill/flask_heroku.git
    $ cd flask_heroku

Second, let's download `pip`, `virtualenv`, `foreman`, and the [`heroku`
Ruby gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo gem install foreman heroku

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate


Installing Packages
--------------------

### Gevent

To use `gevent`, we'll need to install `libevent` for the
`gevent` production server. If you're operating on a Linux OS, you can
`apt-get install libevent-dev`. If you're using Mac OS X, consider
installing the [homebrew](http://mxcl.github.com/homebrew/) package
manager, and run the following command:

    $ brew install libevent

If you're using Mac OS X, you can also install `libevent` through [a DMG
available on Rudix](http://rudix.org/packages-jkl.html#libevent).


### Without Gevent

If you'd rather use `gunicorn` without `gevent`, you just need to edit
the `Procfile` and `requirements.txt`.

First, edit the `Procfile` to look the following:

    web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app

Second, remove `gevent` from the `requirements.txt` file.

### pip

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt


Running Your Application
------------------------

Now, you can run the application locally.

    $ foreman start

You can also specify what port you'd prefer to use.

    $ foreman start -p 5555


Deploying
---------

If you haven't [signed up for Heroku](https://api.heroku.com/signup), go
ahead and do that. You should then be able to [add your SSH key to
Heroku](http://devcenter.heroku.com/articles/quickstart), and also
`heroku login` from the commandline.

Now, to upload your application, you'll first need to do the
following -- and obviously change `app_name` to the name of your
application:

    $ heroku create app_name -s cedar

And, then you can push your application up to Heroku.

    $ git push heroku master
    $ heroku scale web=1

Finally, we can make sure the application is up and running.

    $ heroku ps

Now, we can view the application in our web browser.

    $ heroku open

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate


Next Steps
----------

After you've got your application up and running, there a couple next
steps you should consider following.

1. Create a new `README.md` file.
2. Add your Google Analytics ID to the `base.html` template.
3. Adjust the `author` and `description` `<meta>` tags in the
   `base.html` template.
4. Change the `humans.txt` and `favicon.ico` files in the `static`
   directory.
5. Change the `apple-touch` icons in the `static` directory.


Reactivating the Virtual Environment
------------------------------------

If you haven't worked with `virtualenv` before, you'll need to
reactivate the environment everytime you close or reload your terminal.

    $ source env/bin/activate

If you don't reactivate the environment, then you'll probably receive a
screen full of errors when trying to run the application locally.


Adding Requirements
-------------------

In the course of creating your application, you may find yourself
installing various Python modules with `pip` -- in which case you'll
need to update the `requirements.txt` file. One way that this can be
done is with `pip freeze`.

    $ pip freeze > requirements.txt


Custom Domains
--------------

If your account is verified -- and your credit card is on file -- you
can also easily add a custom domain to your application.

    $ heroku addons:add custom_domains
    $ heroku domains:add www.mydomainname.com

You can add a [naked domain
name](http://devcenter.heroku.com/articles/custom-domains), too.

    $ heroku domains:add mydomainname.com

Lastly, add the following A records to your DNS management tool.

    75.101.163.44
    75.101.145.87
    174.129.212.2
