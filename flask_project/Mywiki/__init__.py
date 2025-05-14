from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('Mywiki.config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .models import article

import Mywiki.views