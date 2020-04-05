from task_lister import db,login,local,now
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    mob = db.Column(db.BigInteger(),unique = True)
    password_hash = db.Column(db.String(120))
    tasks = db.relationship('Task', backref = 'user', lazy = 'dynamic', cascade = 'all, delete-orphan')

    def __repr__(self):
        return 'User {}'.format(self.username)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return  check_password_hash(self.password_hash, password)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    t_name = db.Column(db.String(20))
    t_desc = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime, index = True, default = now.replace(tzinfo = local))
    ddate = db.Column(db.DateTime, index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return 'Task {}'.format(self.t_name)    
