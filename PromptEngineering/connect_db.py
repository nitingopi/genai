# connect to redshift database using redshift_connector library
# return the connection object

import redshift_connector

def connect_to_redshift(host, port, user, password, dbname):
    conn = redshift_connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=dbname
    )
    return conn