from flask_sqlalchemy import SQLAlchemy
from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    video_url = db.Column(db.String(300), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Video('{self.title}', '{self.product_name}')"
