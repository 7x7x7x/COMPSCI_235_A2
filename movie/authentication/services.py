from werkzeug import generate_password_hash, check_password_hash

from movie.adapters.repository_interface import RepositoryInterface
from movie.domain.model import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def add_user(username: str, password: str, repo: RepositoryInterface):
    # verify username not taken
    user = repo.get_user(username)
    print('user got')

    if user is not None:
        raise NameNotUniqueException

    # hash password
    password_hash = generate_password_hash(password)

    # create new user
    user = User(username, password_hash)
    repo.add_user(user)


def get_user(username: str, repo: RepositoryInterface):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    return user


def authenticate_user(username: str, password: str, repo: RepositoryInterface):
    authenticated = False

    user = repo.get_user(username)
    if user is not None:
        print("user pass2: " + password)
        authenticated = check_password_hash(user.password, password)

    if not authenticated:
        raise AuthenticationException



