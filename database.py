from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Perry!1507@localhost:5432/postgres"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False,autocomit = False, bind = engine)