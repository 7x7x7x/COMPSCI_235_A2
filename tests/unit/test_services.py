import pytest

from movie.authentication.services import AuthenticationException
from movie.utilities import services as util_services
from movie.authentication import services as auth_services
from movie.content import services as cont_services


def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_return = auth_services.get_user(new_username, in_memory_repo)
    assert user_return.user_name == new_username

    # Check that password has been encrypted.
    assert user_return.password.startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)


def test_search_movie(in_memory_repo):
    result = cont_services.search("dark knight", "movie", in_memory_repo)

    assert len(result) == 2


def test_search_actor(in_memory_repo):
    result = cont_services.search("hayden", "actor", in_memory_repo)

    assert len(result) == 2


def test_search_genre(in_memory_repo):
    result = cont_services.search("horror", "genre", in_memory_repo)

    assert len(result) > 0


# count search not need testing as it is the same as search but faster and shows only number of entries in repo

def test_most_viewed(in_memory_repo):
    in_memory_repo.add_view('testMovie', 20)

    assert util_services.get_most_viewed(in_memory_repo)[0][0] == 'testMovie'
    assert util_services.get_most_viewed(in_memory_repo)[0][1] == 20


def test_random_movies(in_memory_repo):
    assert len(util_services.get_random_movies(10, in_memory_repo)) == 10


def test_construct_trailer_url(in_memory_repo):
    assert cont_services.get_trailer("Guardians of the Galaxy", in_memory_repo) == "https://www.youtube.com/embed/d96cjJhvlMA"