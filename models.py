import datetime

from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(Model):
	username = Charfield(unique = True)
	email = Charfield(unique = True)
	password = Charfield(max_length=100)
	joinerd_at = DateTimeField(default=datetime.datetime.now)
	is_admin = Boolean(default=False)

	class Meta:
		database = DATABASE
		order_by = ('-joined_at',)

