from movie.adapters.repository_interface import RepositoryInterface


def movie_filter_year(year, repo: RepositoryInterface):
    r_list = repo.movie_filter_year(year)
    return r_list


def count_search(search_term: str, category: str, repo: RepositoryInterface):
    count = 0
    if category == 'movie':
        mv_list = repo.get_movie_list()
        for mv in mv_list:
            if mv.title.lower().find(search_term.lower()) != -1:
                count += 1
    elif category == 'actor':
        actor_list = repo.get_actor_list()
        for actor in actor_list:
            if actor.actor_full_name.lower().find(search_term.lower()) != -1:
                # print("Found: " + actor.actor_full_name.lower() + " with " + search_term.lower())
                # print(count)
                count += 1
    elif category == 'director':
        director_list = repo.get_director_list()
        for director in director_list:
            if director.director_full_name.lower().find(search_term.lower()) != -1:
                count += 1
    elif category == 'genre':
        genre_list = repo.get_genre_list()
        for genre in genre_list:
            if genre.genre_name.lower().find(search_term.lower()) != -1:
                count += 1

    return count


def search(search_term: str, category: str, repo: RepositoryInterface):
    mv_list = repo.get_movie_list()

    r_list = []

    if category == 'movie':
        for mv in mv_list:
            if mv.title.lower().find(search_term.lower()) != -1:
                r_list.append(mv)
    elif category == 'actor':
        for mv in mv_list:
            # print("Search Actor in: " + mv.title)
            for actor in mv.actors:
                # print(actor.actor_full_name.lower())
                if actor.actor_full_name.lower().find(search_term.lower()) != -1:
                    # print("Found: " + actor.actor_full_name.lower())
                    r_list.append(mv)
    elif category == 'director':
        for mv in mv_list:
            if mv.director.director_full_name.lower().find(search_term.lower()) != -1:
                r_list.append(mv)
    elif category == 'genre':
        for mv in mv_list:
            for genre in mv.genres:
                if genre.genre_name.lower().find(search_term.lower()) != -1:
                    r_list.append(mv)

    return r_list

    # search by year not needed as can directly query


def get_review(movie: str, repo: RepositoryInterface):
    r_list = repo.get_review(movie)

    return r_list


def add_review(movie: str, review: str, repo: RepositoryInterface):
    repo.add_review(movie, review)


def get_views(movie: str, repo: RepositoryInterface):
    return repo.view_count(movie)


def add_views(movie: str, quantity: int, repo: RepositoryInterface):
    repo.add_view(movie, quantity)
