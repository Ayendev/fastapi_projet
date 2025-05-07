from dotenv import load_dotenv
from sqlmodel import SQLModel,create_engine
from models.items import Item
import os

load_dotenv()

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = int(os.getenv("PG_PORT", "5432"))
PG_DB = os.getenv("PG_DB")
#TEST_PG_USER = os.getenv("TEST_PG_USER")
# TEST_PG_PASSWORD = os.getenv("TEST_PG_PASSWORD")
# TEST_PG_HOST = os.getenv("TEST_PG_HOST")
# TEST_PG_PORT = int(os.getenv("TEST_PG_PORT", "3306"))
# TEST_PG_DB = os.getenv("TEST_PG_DB")


#DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}.oregon-postgres.render.com:{PG_PORT}/{PG_DB}"
#TEST_DATABASE_URL = f"postgresql://{TEST_PG_USER}:{TEST_PG_PASSWORD}@{TEST_PG_HOST}:{TEST_PG_PORT}/{TEST_PG_DB}"




engine = create_engine(url=DATABASE_URL, echo=True)

async def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")
    print(e)
