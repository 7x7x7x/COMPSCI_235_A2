from movie.domain.model import User
from movie.domain.model import Actor
from movie.domain.model import Director
from movie.adapters.repository_interface import RepositoryException

import pytest


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_add_user(in_memory_repo):
    user = User('user1', '1234')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('user1') is user


def test_repository_filter_actor(in_memory_repo):
    assert len(in_memory_repo.movie_filter_actor(Actor('Vin Diesel'))) > 0


def test_repository_filter_actor_invalid(in_memory_repo):
    assert len(in_memory_repo.movie_filter_actor(Actor('abc1234'))) == 0


def test_repository_filter_director(in_memory_repo):
    assert len(in_memory_repo.movie_filter_director(Director('James Gunn'))) > 0


def test_repository_filter_director_invalid(in_memory_repo):
    assert len(in_memory_repo.movie_filter_director(Director('abc1234'))) == 0


def test_review(in_memory_repo):
    in_memory_repo.add_review('testMovie', 'test1234')
    assert len(in_memory_repo.get_review('testMovie')) == 1


def test_get_review_empty(in_memory_repo):
    assert len(in_memory_repo.get_review('testMovie2')) == 0


def test_add_view(in_memory_repo):
    in_memory_repo.add_view('testMovie', 1)
    assert in_memory_repo.view_count('testMovie') == 1


def test_view_count(in_memory_repo):
    assert in_memory_repo.view_count('testMovie20') == 0


def test_get_trailer(in_memory_repo):
    assert in_memory_repo.get_trailer("Guardians of the Galaxy") == "d96cjJhvlMA"


def test_get_trailer_none(in_memory_repo):
    assert in_memory_repo.get_trailer(None) == "3cYBfuphkuE"
