from contextlib import contextmanager
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, create_session, Session

from ..configmodule import config


engine = create_engine(config.database.connection_string, future=True)
Base = declarative_base()


def session_factory(**kwargs):
    return create_session(
        bind=engine,
        autocommit=False,
        autoflush=False,
        future=True,
        **kwargs
    )


@contextmanager
def SessionCtx(old_session:Session = None):
    
    if old_session is None:
        session: Session = session_factory()
    else:
        session: Session = old_session
        
    try:
        yield session
    except Exception:
        logger.error('Session rollback because of exception')
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close() 


from .user import User
