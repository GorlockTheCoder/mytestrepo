from flask import Flask

#this is our orm for database connection
from flask_sqlalchemy import SQLAlchemy

#lib resposnsible for data migration
from flask_migrate import Migrate


#instance of our database
db = SQLAlchemy()

# method for creating flask app
def create_app():
    flask_app = Flask(_name_)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

    migrate = Migrate(flask_app, db)
    db.init_app(flask_app)



    return flask_app


