from flask import Blueprint, request, render_template, redirect, url_for, session
import movie.adapters.repository_interface as repo
import movie.content.services as services
from movie.domain.model import Movie, Actor, Director, Genre

from movie.authentication.authentication import login_required

search_blueprint = Blueprint('search_bp', __name__)


@search_blueprint.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search_term')
    category = request.args.get('category')

    if search_term is None or search_term == "":
        # need to add search warning
        return render_template(
            'content/search.html'
        )

    if category == 'year':
        return redirect(url_for('browse_bp.browse_movies_year', year=search_term))
    elif category == 'movie':
        if services.count_search(search_term, 'movie', repo.repository_instance) > 0:
            return redirect(url_for('browse_bp.browse_movies_movie', movie=search_term))
    elif category == 'actor':
        if services.count_search(search_term, 'actor', repo.repository_instance) > 0:
            return redirect(url_for('browse_bp.browse_movies_actor', actor=search_term))
    elif category == 'genre':
        if services.count_search(search_term, 'genre', repo.repository_instance) > 0:
            return redirect(url_for('browse_bp.browse_movies_genre', genre=search_term))
    elif category == 'director':
        if services.count_search(search_term, 'director', repo.repository_instance) > 0:
            return redirect(url_for('browse_bp.browse_movies_director', director=search_term))

    return render_template(
        'content/search.html',
        sr=None
    )
