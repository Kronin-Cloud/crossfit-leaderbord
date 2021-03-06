from flask_security.forms import RegisterForm, Required
from wtforms import StringField


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', [Required()])
    last_name = StringField('Last Name', [Required()])