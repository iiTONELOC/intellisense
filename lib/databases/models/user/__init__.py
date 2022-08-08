import bcrypt
import mysql.connector as mysql_connector
from lib.databases.connection import Connection
from .api_queries import user_queries


class User(Connection):
    def __init__(self, username=None, password=None) -> None:
        super().__init__()
        self.username = str(username)
        self.queries = user_queries
        self.password = password

    @ staticmethod
    def hash_password(password) -> str or None:
        if 'validation_error' not in password:
            return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        else:
            return None

    @ staticmethod
    def check_password(password, hashed_password) -> bool:
        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    def create_user(self):
        'Creates a New User'
        try:
            cnx = self.connection()
            cursor = cnx.cursor(buffered=True)
            query = self.queries['create_user']
            values = (self.username, self.password)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            return self.find_by_name(self.username)
        except mysql_connector.Error as err:
            print(err)
            return err

    def find_by_name(self, name, pwd=False):
        'Gets a User'
        res = None
        data = {}

        try:
            cnx = self.connection()
            cursor = cnx.cursor(buffered=True)
            query = self.queries['get_user_by_name']
            values = (name,)
            cursor.execute(query, values)
            res = cursor.fetchall()
            cursor.close()
            cnx.close()

            if res is not None and len(res) > 0:
                _id, u_name, password = res[0]

                data = {'id': str(_id), 'username': u_name,
                        'password': password}
            if pwd is False:
                data.pop('password')

            return data
        except mysql_connector.Error as err:
            print(err)
            return err

    def find_by_id(self, id, pwd=False):
        'Gets a User'
        res = None
        data = {}
        try:
            cnx = self.connection()
            cursor = cnx.cursor(buffered=True)
            query = self.queries['get_user_by_id']
            values = (id,)
            cursor.execute(query, values)
            res = cursor.fetchall()
            cursor.close()
            cnx.close()
        except mysql_connector.Error as err:
            print(err)
            return err
        finally:
            if res is not None and len(res) > 0:
                _id, u_name, password = res[0]

                data = {'id': str(_id), 'username': u_name,
                        'password': password}

        if pwd is False:
            data.pop('password')
        return data
