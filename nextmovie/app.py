import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#import nmtw
#mov_pred=[]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f28ad3f9573d10852bc8a2d56e7a19ab'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vioahgpttjqzyo:f28bb5e8bd13618a1a853ba6f012978017f09030a40891169690dc8b7591e034@ec2-52-73-155-171.compute-1.amazonaws.com:5432/d9md8urnorsmu9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from nextmovie import routes
