from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#criar arquivo só para setup do database

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import tables
from app.controllers import default

#flask db migrate -m 'nome da migração'