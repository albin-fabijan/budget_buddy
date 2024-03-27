import mysql.connector

from . import config


class Model:
    def connect(self):
        connection = mysql.connector.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.database
        )
        return connection