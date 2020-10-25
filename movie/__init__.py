import os

from flask import Flask
import movie.adapters.repository_interface as repo
from movie.adapters.repository_memory import *


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # test data path
    data_path = os.path.join('movie', 'adapters', 'data', 'Data1000Movies.csv')
    data_path2 = os.path.join('movie', 'adapters', 'data')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
        data_path2 = app.config['TEST_DATA_PATH2']

    # create memory repository
    repo.repository_instance = RepositoryMemory()
    mv_reader = MovieFileCSVReader(data_path)
    mv_reader.read_csv_file()

    load_users(data_path2, repo.repository_instance)
    load_trailers(data_path2, repo.repository_instance)

    for mv in mv_reader.dataset_of_movies:
        repo.repository_instance.add_movie(mv)

    for actor in mv_reader.dataset_of_actors:
        repo.repository_instance.add_actor(actor)

    for director in mv_reader.dataset_of_directors:
        repo.repository_instance.add_director(director)

    for genre in mv_reader.dataset_of_genres:
        repo.repository_instance.add_genre(genre)

    # implement blueprints here
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

        from .content import browse
        app.register_blueprint(browse.browse_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .content import search
        app.register_blueprint(search.search_blueprint)

    return app
