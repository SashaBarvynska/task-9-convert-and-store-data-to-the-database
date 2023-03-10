from peewee import SqliteDatabase

db = SqliteDatabase('data_base', field_types={'uuid': 'text'})
db.connect()
