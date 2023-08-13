# import streamlit as st
from function import connect_db, display_info
from dbinfo import *
import pyodbc

if __name__ == "__main__":
    engine = connect_db(drivername, host, database, query)
    display_info(engine)
    