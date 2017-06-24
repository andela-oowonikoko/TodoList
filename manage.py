from flask import Flask, jsonify, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from config import config
from models import db, User, Todolist

app = Flask(__name__)
app.config.from_object(config['development'])
db.init_app(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Todolist=Todolist)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

@app.route('/createuser', methods=['POST'])
def createuser():
    username = request.json['username']
    password = request.json['password']
    user = User(username=username, password=password)
    user.save()
    return jsonify({'message': 'The User {} has been successfully created'.format(username)})

if __name__ == '__main__':
    manager.run()