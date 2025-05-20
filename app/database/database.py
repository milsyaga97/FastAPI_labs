from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.config.setting import setting

engine = create_engine(setting.url)

session_factory = sessionmaker(bind=engine)

def get_session():
    with session_factory() as session:
        yield session
        session.close()

session_dep = Annotated[Session, Depends(get_session)]
