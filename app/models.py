from app import db
import random


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Text, index=True)

    @classmethod
    def get_random_object(cls):
        rowCount = int(cls.query.count())
        randomRow = cls.query.offset(int(rowCount*random.random())).first()

        return randomRow.number
