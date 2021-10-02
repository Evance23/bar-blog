from . import db,login_manager
from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User (UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email =db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(20),nullable=False, default='default.jpg')
    hashed_password = db.Column(db.String(250)) 
    bio = db.Column(db.String(255),default = 'My default Bio') 
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')