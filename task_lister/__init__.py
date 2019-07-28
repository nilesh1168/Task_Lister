from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from task_lister.config import Config
from flask_login import LoginManager
from dateutil.tz import tzlocal 
from datetime import datetime
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
mail = Mail(app)
login.login_view = 'login'
local = tzlocal()
now = datetime.now()
from task_lister import routes,models