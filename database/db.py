from flask_mongoengine import MongoEngine

database = MongoEngine()


def initialize_db(app):
    database.init_app(app)