
from peewee import SqliteDatabase

from config import Config

db = SqliteDatabase(Config.DATABASE, field_types={'uuid': 'text'})
db.connect()
