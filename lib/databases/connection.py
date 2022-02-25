import mysql.connector
from decouple import config


class Connection:
    def __init__(self, db_name=config('MOVIE_DB_NAME')):
        self.connection = lambda: mysql.connector.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            passwd=config('DB_PWD'),
            database=db_name
        )
