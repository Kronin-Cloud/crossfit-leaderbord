from flask import Flask, render_template, request, redirect, url_for, abort, flash, session
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.orm.exc import NoResultFound
from flask_sendgrid import SendGrid
from flask_script import Manager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user, user_registered
import datetime

app = Flask(__name__)
app.config.from_object('estate.default_settings')
manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, render_as_batch=True)
manager.add_command('db', MigrateCommand)

mail = SendGrid(app)

from estate.models import *
from forms import ExtendedRegisterForm

user_datastore = SQLAlchemyUserDatastore(db, Member, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

mail = Mail(app)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/estate/create/', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        # Form submission
        now = datetime.datetime.now()
        time_end = request.form.get("funding_end_date")
        time_end = datetime.datetime.strptime(time_end, "%Y-%m-%d")


