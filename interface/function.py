"""
Functions to be used in main.py
"""
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy import Text

def connect_db(drivername, host, database, query):
    """
    pass
    """
    url = URL.create(drivername=drivername,
                     host=host,
                     database=database,
                     query=query)


    engine = create_engine(url)
    return engine


def display_info(engine):
    """
    pass
    """
    with engine.connect() as conn:
        print(conn.execute(Text("SELECT CURRENT_USER;")).all())