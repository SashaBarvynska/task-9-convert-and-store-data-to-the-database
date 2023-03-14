from peewee import SqliteDatabase

from config import Config

db = SqliteDatabase(Config.DATA_BASE, field_types={'uuid': 'text'})
db.connect()
