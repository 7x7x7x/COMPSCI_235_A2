import abc
from datetime import date
from movie.domain.model import *

repository_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class RepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def movie_filter_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def movie_filter_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def movie_filter_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def movie_random(self, number: int):
        raise NotImplementedError

    @abc.abstractmethod
    def movie_filter_year(self, year: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre_list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor_list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director_list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, movie: str, review: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_review(self, movie: str):
        raise NotImplementedError

    @abc.abstractmethod
    def add_view(self, movie: str, quantity: int):
        raise NotImplementedError

    @abc.abstractmethod
    def view_count(self, movie: str):
        raise NotImplementedError

    @abc.abstractmethod
    def add_trailer(self, movie: str, yt_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trailer(self, movie: str):
        raise NotImplementedError
