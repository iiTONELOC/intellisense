from decouple import config

from .schema import init
from .queries import movie_queries
from ..connection import Connection
import mysql.connector as mysql_connector


class Movie_DB(Connection):
    def __init__(self, db_name=config('MOVIE_DB_NAME')):
        super().__init__(db_name)
        self.init = lambda: init()
        self.queries = movie_queries

    def save_movie(self, title, img, app_id, link_to_watch):
        res = None
        try:
            cnx = self.connection()
            cursor = cnx.cursor(buffered=True)
            query = self.queries['save_movie']
            values = (title, img, app_id, link_to_watch)
            cursor.execute(query, values)
            records = cursor.fetchall()

            res = records
        except mysql_connector.Error as err:
            print(err)
            return False
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
            return res

    def find_movie_by_title(self, title):
        res = None
        try:
            cnx = self.connection()
            cursor = cnx.cursor(buffered=True)
            query = self.queries['find_movie_by_title']
            cursor.execute(query, (title,))
            records = cursor.fetchall()
            res = records
        except mysql_connector.Error as err:
            print(err)
            return False
        finally:
            cursor.close()
            cnx.close()
            if len(res) > 0:
                return res
            else:
                return False

    def test(self):
        res = None
        try:
            cnx = self.connection()
            cursor = cnx.cursor()
            query = 'SELECT * FROM app'
            cursor.execute(query)
            res = cursor.fetchall()

        except mysql_connector.Error as err:
            print(err)
            return False
        finally:
            cursor.close()
            cnx.close()
            if len(res) > 0:
                return res
            else:
                return False
