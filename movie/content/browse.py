from datetime import date
from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import movie.adapters.repository_interface as repo
import movie.content.services as services
from movie.domain.model import Movie

from movie.authentication.authentication import login_required

browse_blueprint = Blueprint('browse_bp', __name__)


@browse_blueprint.route('/browse_movies_year', methods=['GET'])
def browse_movies_year():
    # query year
    q_year = request.args.get('year')
    q_page = request.args.get('page')

    if q_year is None:
        q_year = 2016
    else:
        q_year = int(q_year)

    if q_page is None:
        q_page = 0
    elif int(q_page) < 0:
        q_page = 0
    else:
        q_page = int(q_page)

    prev_year_url = None
    next_year_url = None

    current_year_raw = services.movie_filter_year(q_year, repo.repository_instance)
    current_year = current_year_raw[(q_page * 8):(q_page * 8 + 8)]

    while len(current_year) < 8:
        current_year.append(Movie(title="...", year=2016))

    # print(current_year_raw)
    # print(current_year)
    # previous_year = services.movie_filter_year(q_year - 1, repo.repository_instance)
    # next_year = services.movie_filter_year(q_year + 1, repo.repository_instance)

    # need to check year valid

    if q_year + 1 > 2016:
        next_year_url = url_for('browse_bp.browse_movies_year', year=2016, page=0)
        prev_year_url = url_for('browse_bp.browse_movies_year', year=(q_year - 1), page=0)
    elif q_year - 1 < 2006:
        next_year_url = url_for('browse_bp.browse_movies_year', year=(q_year + 1), page=0)
        prev_year_url = url_for('browse_bp.browse_movies_year', year=2006, page=0)
    else:
        prev_year_url = url_for('browse_bp.browse_movies_year', year=(q_year - 1), page=0)
        next_year_url = url_for('browse_bp.browse_movies_year', year=(q_year + 1), page=0)

    prev_page_url = url_for('browse_bp.browse_movies_year', year=q_year, page=q_page - 1)
    next_page_url = url_for('browse_bp.browse_movies_year', year=q_year, page=q_page + 1)

    # gen pages
    return render_template(
        'content/browse.html',
        mv_list=current_year,
        prev_year_url=prev_year_url,
        next_year_url=next_year_url,
        prev_page_url=prev_page_url,
        next_page_url=next_page_url,
        featured_title="Showing Year " + str(q_year),
        type="year"
    )


@browse_blueprint.route('/browse_movies_actor', methods=['GET'])
def browse_movies_actor():
    q_name = request.args.get("actor")
    q_page = request.args.get("page")

    if q_page is None:
        q_page = 0
    elif int(q_page) < 0:
        q_page = 0
    else:
        q_page = int(q_page)

    mv_list_raw = services.search(q_name, "actor", repo.repository_instance)
    # print(mv_list_raw)
    mv_list = mv_list_raw[(q_page * 8):(q_page * 8 + 8)]

    prev_page_url = url_for('browse_bp.browse_movies_actor', actor=q_name, page=q_page - 1)
    next_page_url = url_for('browse_bp.browse_movies_actor', actor=q_name, page=q_page + 1)

    while len(mv_list) < 8:
        mv_list.append(Movie(title="...", year=2016))

    # gen pages
    return render_template(
        'content/browse.html',
        mv_list=mv_list,
        prev_year_url="prev_year_url",
        next_year_url="next_year_url",
        prev_page_url=prev_page_url,
        next_page_url=next_page_url,
        featured_title="Showing results for actor: " + q_name,
        type="actor"
    )


@browse_blueprint.route('/browse_movies_director', methods=['GET'])
def browse_movies_director():
    q_name = request.args.get("director")
    q_page = request.args.get("page")

    if q_page is None:
        q_page = 0
    elif int(q_page) < 0:
        q_page = 0
    else:
        q_page = int(q_page)

    mv_list_raw = services.search(q_name, "director", repo.repository_instance)
    # print(mv_list_raw)
    mv_list = mv_list_raw[(q_page * 8):(q_page * 8 + 8)]

    prev_page_url = url_for('browse_bp.browse_movies_director', director=q_name, page=q_page - 1)
    next_page_url = url_for('browse_bp.browse_movies_director', director=q_name, page=q_page + 1)

    while len(mv_list) < 8:
        mv_list.append(Movie(title="...", year=2016))

    # gen pages
    return render_template(
        'content/browse.html',
        mv_list=mv_list,
        prev_year_url="prev_year_url",
        next_year_url="next_year_url",
        prev_page_url=prev_page_url,
        next_page_url=next_page_url,
        featured_title="Showing results for director: " + q_name,
        type="director"
    )


@browse_blueprint.route('/browse_movies_movie', methods=['GET'])
def browse_movies_movie():
    q_name = request.args.get("movie")
    q_page = request.args.get("page")

    if q_page is None:
        q_page = 0
    elif int(q_page) < 0:
        q_page = 0
    else:
        q_page = int(q_page)

    mv_list_raw = services.search(q_name, "movie", repo.repository_instance)
    # print(mv_list_raw)
    mv_list = mv_list_raw[(q_page * 8):(q_page * 8 + 8)]

    prev_page_url = url_for('browse_bp.browse_movies_movie', genre=q_name, page=q_page - 1)
    next_page_url = url_for('browse_bp.browse_movies_movie', genre=q_name, page=q_page + 1)

    while len(mv_list) < 8:
        mv_list.append(Movie(title="...", year=2016))

    # gen pages
    return render_template(
        'content/browse.html',
        mv_list=mv_list,
        prev_year_url="prev_year_url",
        next_year_url="next_year_url",
        prev_page_url=prev_page_url,
        next_page_url=next_page_url,
        featured_title="Showing results for movie: " + q_name,
        type="movie"
    )


@browse_blueprint.route('/browse_movies_genre', methods=['GET'])
def browse_movies_genre():
    q_name = request.args.get("genre")
    q_page = request.args.get("page")

    if q_page is None:
        q_page = 0
    elif int(q_page) < 0:
        q_page = 0
    else:
        q_page = int(q_page)

    mv_list_raw = services.search(q_name, "genre", repo.repository_instance)
    # print(mv_list_raw)
    mv_list = mv_list_raw[(q_page * 8):(q_page * 8 + 8)]

    prev_page_url = url_for('browse_bp.browse_movies_genre', genre=q_name, page=q_page - 1)
    next_page_url = url_for('browse_bp.browse_movies_genre', genre=q_name, page=q_page + 1)

    while len(mv_list) < 8:
        mv_list.append(Movie(title="...", year=2016))

    # gen pages
    return render_template(
        'content/browse.html',
        mv_list=mv_list,
        prev_year_url="prev_year_url",
        next_year_url="next_year_url",
        prev_page_url=prev_page_url,
        next_page_url=next_page_url,
        featured_title="Showing results for genre: " + q_name,
        type="genre"
    )


# spaghetti code alert
@browse_blueprint.route('/movie_info', methods=['GET', 'POST'])
def movie_info():
    try:
        username = session['username']
    except KeyError:
        username = "Anon"

    form = CommentForm()

    # POST
    if form.validate_on_submit():
        movie_name = form.movie_name.data

        # call service to store comment
        services.add_review(movie_name, '"' + form.comment.data + '" - ' + username, repo.repository_instance)
        print('POST sucess')
        # refresh page
        return redirect(url_for('browse_bp.movie_info', movie=movie_name))

    # GET
    if request.method == 'GET':
        q_name = request.args.get("movie")
        # form.movie_name.data = q_name
        # services.add_views(q_name, 1, repo.repository_instance)
        # movie_desc = "..."

        # review = services.get_review(q_name, repo.repository_instance)
        # views = services.get_views(q_name, repo.repository_instance)
        # s_query = services.search(q_name, 'movie', repo.repository_instance)
        # trailer = services.get_trailer(q_name, repo.repository_instance)

        # if len(s_query) != 0:
        #    movie_desc = s_query[0].description
    else:
        q_name = form.movie_name.data

    # q_name = request.args.get("movie")

    movie_desc = "..."

    review = services.get_review(q_name, repo.repository_instance)
    views = services.get_views(q_name, repo.repository_instance)
    s_query = services.search(q_name, 'movie', repo.repository_instance)
    trailer = services.get_trailer(q_name, repo.repository_instance)

    if len(s_query) != 0:
        movie_desc = s_query[0].description

    form.movie_name.data = q_name
    services.add_views(q_name, 1, repo.repository_instance)

    return render_template(
        'content/movie_info.html',
        featured_title=q_name,
        handler_url=url_for('browse_bp.movie_info', movie=q_name),
        form=form,
        review=review,
        movie_views=views,
        movie_desc=movie_desc,
        movie_trailer_url=trailer
    )


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short')])
    movie_name = HiddenField("movie_name")
    submit = SubmitField("Submit")
