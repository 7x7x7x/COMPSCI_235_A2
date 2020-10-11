from flask import Blueprint, render_template, url_for, redirect, session

import movie.adapters.repository_interface as repo
import movie.utilities.services as services

# blueprint init
utilities_blueprint = Blueprint(
    'utilities_bp', __name__
)


def retrieve_movie_random():
    return services.get_random_movies(10, repo.repository_instance)