from movie.domain.model import User, Movie, Actor, Director

import pytest


@pytest.fixture()
def movie():
    mv = Movie("test", 2016)
    mv.add_actor(Actor('actor1'))
    mv.director = Director('director1')

    return mv


@pytest.fixture()
def user():
    return User('mjackson', 'vpwJv4A7%#9b')


def test_user_construction(user):
    assert user.user_name == 'mjackson'
    assert user.password == 'vpwJv4A7%#9b'


def test_movie_construction(movie):
    assert movie.actors[0].actor_full_name == 'actor1'
    assert movie.director.director_full_name == 'director1'
    assert movie.title == 'test'
    assert movie.year == 2016


