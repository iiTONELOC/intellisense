from __future__ import print_function
from decouple import config
import mysql.connector
from mysql.connector import errorcode

DB_NAME = config('DB_NAME')

TABLES = {}
TABLES['app'] = (
    "CREATE TABLE `app` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `name` varchar(55) NOT NULL UNIQUE KEY"
    ") ENGINE=InnoDB")

TABLES['movie'] = (
    "CREATE TABLE `movie` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `title` varchar(300) NOT NULL UNIQUE,"
    "  `app_id` int(11) NOT NULL,"
    "  `img` text NOT NULL,"
    "  `url` varchar(500) NOT NULL,"
    "  FOREIGN KEY (`app_id`) REFERENCES `app` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['user'] = (
    "CREATE TABLE `user` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `username` varchar(55) NOT NULL UNIQUE,"
    "  `password` varchar(150) NOT NULL"
    ") ENGINE=InnoDB"
)


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def init():
    cnx = mysql.connector.connect(
        user=config('DB_USER'), passwd=config('DB_PWD'))

    cursor = cnx.cursor()
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            cursor.execute(table_description)

        # SEED THE APP TABLE WITH THE STREAMING APP, CURRENTLY ONLY NETFLIX
            if table_name == 'app':
                cursor.execute("INSERT INTO app (name) VALUES ('Netflix')")

        except mysql.connector.Error:
            pass

    cursor.buffered = True
    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    init()
