#!flask/bin/python
'''
This module contains the following to set up API Endpoints
    - URL Routing
    - Basic/Digest authentication
'''
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth,HTTPDigestAuth
from backend import tasks, users 
import os
app = Flask(__name__)
app.config.from_pyfile('config.py') #adding secure key for authentication as a config

'''
Authentication implementation
'''

# Digest authentication
digest_auth = HTTPDigestAuth()
@digest_auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# Digest authentication error handler
@digest_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
basic_auth = HTTPBasicAuth()

# Basic authentication
@basic_auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

# Basic authentication error handler
@basic_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

'''
URL Routing specification
'''

# return String
@app.route('/')
def index():  
    return "Hello, World from Heroku!"
    

# For a given task (refer backend.py), generate the URL endpoint for the task id key   
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

# HTTP GET method
# Requires basic authentication (refer backend.py to configure username/password)
# User @digest_auth.login_required, for digest authentication
# Returns all tasks from the backend, if the authentication is successful
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@basic_auth.login_required
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

# HTTP GET
# For a given task id, returns the task from the backend
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# HTTP POST
# Adds the task provided to the backend
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# HTTP PUT
# Updates the task for the given task id
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# HTTP DELETE
# Deletes the task for the given task id
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

'''
Returns json with error description
'''
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)