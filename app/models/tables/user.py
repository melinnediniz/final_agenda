from app import db


class User(db.Model):
    __tablebname__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    
    def __init__(self, username, email, password, name):
        self.email = email
        self.username = username
        self.name = name
        self.password = password
    
    def __repr__(self):
        return "<User-%r>" % self.id