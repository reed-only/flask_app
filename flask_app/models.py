# pylint: disable=no-member
"""
Data models
"""

from flask_app.extensions import db


class Bananas(db.Model):
    """bananas"""
    __tablename__ = 'bananas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(45))
    weight = db.Column(db.Float)


class Toast(db.Model):
    """toast"""
    __tablename__ = 'toast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    toastiness = db.Column(db.String(45))
