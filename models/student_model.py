from db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(120), nullable= True)

    def __repr__(self):
        return '<id %r>' % self.id