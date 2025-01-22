from flask import Flask
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "keep it secret"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')