from movie.adapters.repository_interface import RepositoryInterface


def get_random_movies(quantity, repo: RepositoryInterface):
    movies = repo.movie_random(quantity)

    return movies


def get_most_viewed(repo: RepositoryInterface):
    v_list = repo.view_count(None)
    print(v_list)
    v_list_sorted = sorted(v_list.items(), key=lambda item: item[1], reverse=True)
    print(v_list_sorted)

    return v_list_sorted
