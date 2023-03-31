from app import db


class Event(db.Model):
    __tablebname__ = "event"
    evento_id = db.Column(db.Integer, primary_key=True, nullable=False)
    evento_title = db.Column(db.String(80), unique=True, nullable=False)
    evento_descriptiom = db.Column(db.String(120), unique=True, nullable=False)
    evento_status = db.Column(db.Integer, nullable=False)
    
    
    def __init__(self, title, description, status):
        self.evento_title = title
        self.evento_description = description
        self.evento_status = status
    
    def __repr__(self):
        return "<Event-%r>" % self.id