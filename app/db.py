from pathlib import Path

from sqlmodel import create_engine, SQLModel

from app.model import create_all


BaseDir = Path(__file__).resolve().parent.parent


sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{BaseDir}/{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    create_all()
    SQLModel.metadata.create_all(engine)
