import os

from dotenv import load_dotenv
load_dotenv(".env")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
SYNC_URL= f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT }/{ DB_NAME}'
ECHO = True
AUTOCOMMIT = False
AUTOFLUSH =False
