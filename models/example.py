from peewee import CharField, BooleanField, SmallIntegerField, DateField, ForeignKeyField, UUIDField

from models import BaseModel, db


class Example(BaseModel):
    title = CharField(null=False, verbose_name="标题")