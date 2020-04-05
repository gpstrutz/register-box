from .db import database

class User(database.Document):
    name = database.StringField(required=True, unique=True)
    total_value = database.DecimalField(precision=2, force_string=False, required=True)
    payment_value = database.DecimalField(precision=2, force_string=False, required=True)
