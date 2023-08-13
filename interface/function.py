from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL  # Import URL from the engine submodule
from sqlalchemy import text


def connect_remote(drivername, username, password, host, port, database, query):
    """
    pass
    """
    try:
        url = URL.create(drivername=drivername,
                         username=username,
                         password=password,
                         host=host,
                         port=port,
                         database=database,
                         query=query)
        engine = create_engine(url)
        return engine
    except:
        raise ValueError("Engine object could not be created")


def display_info(engine):
    """
    pass
    """
    with engine.connect() as conn:
        sql = text("SELECT CURRENT_USER;")
        result = conn.execute(sql).all()
        if result:
            return str(result[0][0])
        else:
            return None