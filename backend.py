'''
tasks is a dictionary. This can be modifed by the API's defined in app.py
users is a dictionary containing username and password. If a API method in app.py enforces auth,
    the username and password must match, as specified here. 
Use hashing when storing and transmitting passwords in Production.
'''
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

users = {
    "John": "JohnHasAStrongPassword@1",
    "Alice": "password"
}