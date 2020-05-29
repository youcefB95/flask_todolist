import argparse
import logging

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bootstrap import Bootstrap

db = SQLAlchemy()


def create_app(config_obj='test'):
    app = Flask(__name__,instance_relative_config=True)
    app.logger.addHandler(logging.StreamHandler())
    bootstrap = Bootstrap(app)
    cors = CORS(app)

    #Load config from config folder
    app.config.from_object('config.config.{0}'.format(config_obj))

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    from . import views
    app.register_blueprint(views.blueprint)

    with app.app_context():
        db.init_app(app)
        from app import views
        from app.tables import Task
        db.create_all()

    return app


def create_parser():

    parser = argparse.ArgumentParser(
        description="",
    )
    parser.add_argument(
       "--host", "-H",
       type=str,
       default=None,
    )
    parser.add_argument(
       "--port", "-P",
       type=int,
       default=None,
    )
    parser.add_argument(
       "--debug", "-D",
       type=bool,
       default=False,
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        default="test",
    )
    return parser

