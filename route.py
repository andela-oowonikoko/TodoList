from flask import jsonify, request

from manage import app
from models import User, Todolist

print('route\'s up!')


@app.route('/createuser', methods=['POST'])
def createuser():
    username = request.json['username']
    password = request.json['password']
    user = User(username=username, password=password)
    user.save()
