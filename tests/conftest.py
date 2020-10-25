import os
import pytest

from movie import create_app
from movie.adapters.repository_memory import *

from movie.adapters.repository_memory import RepositoryMemory

# change the test data target to respective directories
TEST_DATA_PATH = os.path.join('tests', 'data', 'Data1000Movies.csv')
TEST_DATA_PATH2 = os.path.join('tests', 'data')


@pytest.fixture
def in_memory_repo():
    repo = RepositoryMemory()
    mv_reader = MovieFileCSVReader(TEST_DATA_PATH)
    mv_reader.read_csv_file()
    load_users(TEST_DATA_PATH2, repo)
    load_trailers(TEST_DATA_PATH2, repo)

    for mv in mv_reader.dataset_of_movies:
        repo.add_movie(mv)

    for actor in mv_reader.dataset_of_actors:
        repo.add_actor(actor)

    for director in mv_reader.dataset_of_directors:
        repo.add_director(director)

    for genre in mv_reader.dataset_of_genres:
        repo.add_genre(genre)

    return repo


@pytest.fixture
def client():
    my_app = create_app({'TESTING': True, 'TEST_DATA_PATH': TEST_DATA_PATH, 'TEST_DATA_PATH2': TEST_DATA_PATH2, 'WTF_CSRF_ENABLED': False})

    return my_app.test_client()


class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='thorke', password='cLQ^C#oFXloS'):
        return self._client.post(
            'authentication/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/authentication/logout')


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)
