from estate import db, app
from sqlalchemy.sql import func
from flask_security import RoleMixin, UserMixin
import datetime

roles_members = db.Table('roles_members',
                         db.Column('member_id', db.Integer(), db.ForeignKey('member.id')),
                         db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Member(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Estate(db.Model):
    id = db.Column(db.Integer(), primary_key=True)