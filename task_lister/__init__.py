from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from task_lister.config import Config
from flask_login import LoginManager
from dateutil.tz import * 
from datetime import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'
local = tzlocal()
now = datetime.now()
from task_lister import routes,models