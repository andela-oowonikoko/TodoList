from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CRUDMixin(object):
    date_created = db.Column(db.DateTime, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(CRUDMixin, db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String(8))

    def __repr__(self):
        return 'User: {}'.format(self.username)

class Todolist(CRUDMixin, db.Model):
    __tablename__ = 'todolists'
    taskId = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String)

    def __repr__(self):
        return 'Task Id: {}'.format(self.taskId)