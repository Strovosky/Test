from codecs import unicode_escape_decode
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Integer, String, BigInteger

Base = declarative_base()

class Student(Base):
    __tablename__ = "Student"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=30), nullable=False, unique=True)
    email = Column(String(length=30), nullable=False, unique=True)
    phone = Column(BigInteger(), nullable=True, unique=False)

    def __str__(self) -> str:
        return self.name
