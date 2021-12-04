from dataclasses import dataclass, asdict


@dataclass
class DataSQLiteToPostgres:

    @property
    def get_values(self):
        return '\t'.join([str(value) for value in asdict(self).values()])


@dataclass
class Movie(DataSQLiteToPostgres):
    id: str
    title: str
    description: str
    creation_date: str
    certificate: str
    file_path: str
    rating: float
    type: str
    created_at: str
    updated_at: str


@dataclass
class Genre(DataSQLiteToPostgres):
    id: str
    name: str
    description: str
    created_at: str
    updated_at: str


@dataclass
class Person(DataSQLiteToPostgres):
    id: str
    full_name: str
    birth_date: str
    created_at: str
    updated_at: str


@dataclass
class GenreFilmWork(DataSQLiteToPostgres):
    id: str
    film_work_id: str
    genre_id: str
    created_at: str


@dataclass
class PersonFilmWork(DataSQLiteToPostgres):
    id: str
    film_work_id: str
    person_id: str
    role: str
    created_at: str
