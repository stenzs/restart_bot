from peewee import *
import config

db = PostgresqlDatabase(database=config.database, user=config.user, password=config.password, host=config.host, port=config.port)


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = PrimaryKeyField(column_name='id', primary_key=True, unique=True)
    number = IntegerField(column_name='number')


    class Meta:
        table_name = 'users'

db.create_tables([Users])