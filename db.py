from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# db variable is SQLAlchemy object that will link to flask app and look at all objects we tell it to and
# allow us to map those objects to rows in a database
