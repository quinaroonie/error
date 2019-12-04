# models.py
import os, flask_sqlalchemy, app
import flask_socketio


# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://purple:purpleisawesome@localhost/postgres'


db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(120))
    username = db.Column(db.String(120)) 
    image = db.Column(db.String(120))
    
    def __init__(self, t):
        self.text = t
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 


