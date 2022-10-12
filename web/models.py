from sqlalchemy import func
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, nullable=False, default=5)
    address = db.Column(db.String(1000), nullable=True)
    city = db.Column(db.String(150), nullable=True)
    state = db.Column(db.String(150), nullable=True)
    postal_code = db.Column(db.String(25), nullable=True)
    country = db.Column(db.String(150), nullable=True)
    nickname = db.Column(db.String(150), nullable=True)
    organization = db.Column(db.String(1000), nullable=True, unique=True)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(1000), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('course_category.id'))
    description = db.Column(db.String(1000), nullable=False)
    content = db.Column(db.BLOB, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    enrolled = db.Column(db.Boolean, default=False)


class CourseCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    parent_id = db.Column(db.Integer)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.BLOB, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    course_id = db.Column(
        db.Integer, db.ForeignKey('course.id'), nullable=True)
