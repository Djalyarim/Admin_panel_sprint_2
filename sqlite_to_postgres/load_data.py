import io
import os

import sqlite3

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from dotenv import load_dotenv

from data_classes import Movie, Person, Genre, GenreFilmWork, PersonFilmWork
from custom_log import log

load_dotenv()

TABLES_CLASSES = {
    'film_work': Movie,
    'genre': Genre,
    'person': Person,
    'genre_film_work': GenreFilmWork,
    'person_film_work': PersonFilmWork,
}


class SQLiteLoader:
    def __init__(self, connection, table_name, data_class):
        self.connection = connection
        self.table_name = table_name
        self.data_class = data_class
        self.cursor = self.connection.cursor()
        self.cursor.execute(f'SELECT * FROM {self.table_name}')

    def load_movies(self):
        while True:
            part_of_lines = self.cursor.fetchmany(50)
            if not part_of_lines:
                break
            block = []
            for line in part_of_lines:
                data = self.data_class(*line)
                block.append(data)
            yield block

    def __del__(self):
        self.cursor.close()


class PostgresSaver(SQLiteLoader):

    def save_all_data(self, data):
        for part in data:
            part_values = '\n'.join([object.get_values for object in part])
            with io.StringIO(part_values) as f:
                self.cursor.copy_from(
                    f,
                    table=self.table_name,
                    null='None',
                    size=50
                )


def load_from_sqlite(sql_conn: sqlite3.Connection, psg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    for table_name, data_class in TABLES_CLASSES.items():
        try:
            sqlite_loader = SQLiteLoader(sql_conn, table_name, data_class)
            data = sqlite_loader.load_movies()
        except Exception:
            log.exception('Ошибка во время чтения SQLite')
            break
        try:
            postgres_saver = PostgresSaver(psg_conn, table_name, data_class)
            postgres_saver.save_all_data(data)
        except Exception:
            log.exception('Ошибка во время записи в Postgres')
            break
        else:
            log.info(f'Таблица {table_name} загружена')


if __name__ == '__main__':
    dsl = {
        'dbname': os.getenv('POSTGRES_DB'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'host': os.getenv('DB_LOCAL_HOST'),
        'port': os.getenv('DB_PORT'),
        'options': '-c search_path=content'
    }
    with (sqlite3.connect('db.sqlite') as sqlite_conn,
          psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn):
        load_from_sqlite(sqlite_conn, pg_conn)

    sqlite_conn.close()
