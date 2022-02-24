from __future__ import print_function
from decouple import config
import mysql.connector
from mysql.connector import errorcode

MOVIE_DB_NAME = config('MOVIE_DB_NAME')

TABLES = {}
TABLES['app'] = (
    "CREATE TABLE `app` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `name` varchar(55) NOT NULL UNIQUE KEY"
    ") ENGINE=InnoDB")

TABLES['movie'] = (
    "CREATE TABLE `movie` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `title` varchar(255) NOT NULL,"
    "  `app_id` int(11) NOT NULL,"
    "  `img` varchar(255) NOT NULL,"
    "  `url` varchar(255) NOT NULL,"
    "  FOREIGN KEY (`app_id`) REFERENCES `app` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MOVIE_DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def init():
    cnx = mysql.connector.connect(
        user=config('DB_USER'), passwd=config('DB_PWD'))

    cursor = cnx.cursor()
    try:
        cursor.execute("USE {}".format(MOVIE_DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(MOVIE_DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(MOVIE_DB_NAME))
            cnx.database = MOVIE_DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    init()
