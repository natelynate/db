"""
Parameter settings for establishing DB Connection
"""

## Local connections
# drivername = "mssql+pyodbc"
# host = "DESKTOP-K2TBT87\SQLEXPRESS"
# database = "trade_network_db"
# query = {"trusted_connection":"Yes",
#          "driver":"ODBC Driver 17 for SQL Server"}

##  Remote Connections
drivername = "mssql+pyodbc"
host = "192.168.0.2"
database = "trade_network_db"
port = 49172
username = 'defaultuser' 
password = 'user123'
query = {"trusted_connection":"No",
         "driver":"SQL Server"}
