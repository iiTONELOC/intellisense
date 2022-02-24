from decouple import config
from .schema import init
from ..connection import Connection


class Movie_DB(Connection):
    def __init__(self, db_name=config('MOVIE_DB_NAME')):
        super().__init__(db_name)
        self.cursor = lambda: self.connection.cursor()
        self.init = lambda: init()
