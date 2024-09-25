from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging

import os 

env_path = env_path = os.path.join(os.path.dirname(__file__), '/../.env')
print(os.path.dirname(__file__))
load_dotenv(dotenv_path=env_path)



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



#проверка переменных окружения
POSTGRES_USER = os.getenv('POSTGRES_USER','myuser')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD','mypassword')
POSTGRES_DB = os.getenv('POSTGRES_DB','mydatabase')
POSTGRES_HOST = os.getenv('POSTGRES_HOST','localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT','5444')


# POSTGRES_USER=myuser
# POSTGRES_PASSWORD=mypassword
# POSTGRES_DB=mydatabase
# POSTGRES_HOST=localhost
# POSTGRES_PORT=5432

# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
DATABASE_URL = f"postgresql://myuser:mypassword@db:5432/mydatabase"
# DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

except Exception as e:
    logger.error(f"Failed to connect to the database: {e}")
    raise
def init_db():
    Base.metadata.create_all(bind=engine)