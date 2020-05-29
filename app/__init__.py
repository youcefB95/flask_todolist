from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

app = Flask(__name__,instance_relative_config=True)
bootstrap = Bootstrap(app)
cors = CORS(app)
app.config.from_object('config.config.TestingConfig')


# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


with app.app_context():
    db.init_app(app)
    from app import views
    from app.tables import Task
    db.create_all()
