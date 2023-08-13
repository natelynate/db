# import streamlit as st
from function import connect_remote, display_info
from dbinfo import drivername, username, password, host, port, database, query
import pyodbc

if __name__ == '__main__':
    engine = connect_remote(drivername, username, password, host, port, database, query)
    fetched = display_info(engine)
    if fetched:
        print("=" * 50)
        print(f"Successfully connected as {fetched}.")
        