from decouple import config

from .models.user import User
from .models.schema import init
from .models.movies import Movies
from .connection import Connection


class DB(Connection):
    def __init__(self, db_name=config('DB_NAME')):
        super().__init__(db_name)
        self.init = lambda: init()
        self.models = {'movies': Movies(), 'user': User}
