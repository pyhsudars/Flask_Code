#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db

def createApp():
    import dbConfig

    app = Flask(__name__)
    from demandApp import demandApp
    import dbConfig

    app.config.from_object(dbConfig.Config)
    app.register_blueprint(demandApp)
    # db.init_app(app)
    # migrate = Migrate(app, db)
    return app
