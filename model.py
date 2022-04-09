from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Integer,
    String,
    Text,
    DateTime,
    Float,
    Boolean,
)

db = SQLAlchemy()


class PeopleModel(db.Model):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    about = Column(Text)
    birthdate = Column(DateTime)
    height = Column(Float)
    single = Column(Boolean)