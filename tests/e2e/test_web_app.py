import pytest

from flask import session


def test_register(client):
    # Retrieve register page
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Register user

    response = client.post('/authentication/register', data={'username': 'gmichael', 'password': 'CarelessWhisper1984'})
    assert response.headers['Location'] == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('cj', '', b'Your username is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test',
         b'Your password must at least 8 characters, and contain an upper case letter, a lower case letter and a digit'),
        ('fmercury', 'Test#6^0', b'Username already taken'),
))
def test_register_with_invalid_input(client, username, password, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['username'] == 'thorke'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_homepage(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200


def test_review(client, auth):
    auth.login()

    response = client.get('/movie_info?movie=Split')
    # assert response.status_code == 200

    response = client.post(
        '/movie_info',
        data={'comment': 'sick film', 'movie_name': 'Split'}
    )

    assert response.headers['Location'] == 'http://localhost/movie_info?movie=Split'


def test_year_without_date(client):
    response = client.get('/browse_movies_year')
    assert response.status_code == 200

    assert b'Split' in response.data


def test_search_movie_invalid(client):
    response = client.get('/search?search_term=hayden&category=movie')
    assert response.status_code == 200

    assert b'No results' in response.data


def test_search_director_invalid(client):
    response = client.get('/search?search_term=zzzaaazzzaazzaaz&category=director')
    assert response.status_code == 200

    assert b'No results' in response.data


def test_search_actor_invalid(client):
    response = client.get('/search?search_term=zzzaaazzzaazzaaz&category=actor')
    assert response.status_code == 200

    assert b'No results' in response.data


def test_search_actor(client):
    response = client.get('/search?search_term=hayden&category=actor')
    # assert response.status_code == 200
    assert response.headers['Location'] == 'http://localhost/browse_movies_actor?actor=hayden'


def test_search_genre(client):
    response = client.get('/search?search_term=horror&category=genre')
    # assert response.status_code == 200
    assert response.headers['Location'] == 'http://localhost/browse_movies_genre?genre=horror'


def test_search_director(client):
    response = client.get('/search?search_term=james&category=director')
    # assert response.status_code == 200
    assert response.headers['Location'] == 'http://localhost/browse_movies_director?director=james'


def test_search_year(client):
    response = client.get('/search?search_term=2016&category=year')
    # assert response.status_code == 200
    assert response.headers['Location'] == 'http://localhost/browse_movies_year?year=2016'
