from src.extensions.db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))