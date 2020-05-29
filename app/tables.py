# coding: utf-8
import json

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    category = db.Column(db.Integer)

    def __init__(self,content, category):
        self.content = content
        self.category = category

    # def __repr__(self):
    #     json_obj = {
    #         "id": self.id,
    #         "content": self.content,
    #         "category": self.category
    #     }
    #     return json.dumps(json_obj)
