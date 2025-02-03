from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(36), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    cookies = db.Column(db.Integer, default=0)
    cursors = db.Column(db.Integer, default=0)
    grandmas = db.Column(db.Integer, default=0)
    factories = db.Column(db.Integer, default=0)
    booster_modifier = db.Column(db.Integer, default=1)
