from flask import Blueprint, render_template, url_for
import movie.utilities.services as services
import movie.adapters.repository_interface as repo

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    browse_movies_url = url_for('browse_bp.browse_movies_year', year=2016)
    login_url = url_for('authentication_bp.login')
    mv_list = services.get_random_movies(12, repo.repository_instance)
    top_list = services.get_most_viewed(repo.repository_instance)
    # print(top_list)

    while len(top_list) < 4:
        top_list.append(("...", 2016))

    return render_template(
        'home/home.html',
        mv_list=mv_list,
        browse_movies_url=browse_movies_url,
        login_url=login_url,
        top_list=top_list
    )
