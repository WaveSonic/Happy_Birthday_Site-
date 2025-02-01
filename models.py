from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    device_id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    clicks = db.Column(db.Integer, default=0)
    booster_modifier = db.Column(db.Integer, default=1)

    def __init__(self, device_id, username):
        self.device_id = device_id
        self.username = username
