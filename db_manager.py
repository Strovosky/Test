from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from models import Base


engine = create_engine("mysql+pymysql://your_user:your_password@localhost:3306/university1")

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
