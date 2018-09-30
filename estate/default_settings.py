import os

DEBUG = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"
SQLALCHEMY_TRACK_MODIFICATIONS= True

SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECRET_KEY = "\xf3\xd2\xb0\xad\x8e\x81\x05\x96Z\xf5\tB\x0c\x8b\xef\x0e\x10b+KQ\xe0q\x02"
SENDGRID_DEFAULT_FROM="estate@kronin.cloud"
SENDGRID_API_KEY= os.environ.get("SENDGRID_API_KEY")

