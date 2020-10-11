from datetime import datetime


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleagues:
            return True
        else:
            return False


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        # TODO
        if self.__director_full_name == other.director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        # TODO
        if self.__director_full_name < other.director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        # TODO
        return hash(self.__director_full_name)


class Genre:
    def __init__(self, g_name: str):
        if g_name == "" or type(g_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = g_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.genre_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__genre_name < other.genre_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__genre_name)


class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

        if type(year) is not int or year < 1900:
            self.__year = None
        else:
            self.__year = year

        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        if new_title == "" or type(new_title) is not str:
            pass
        else:
            self.__title = new_title.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 1900:
            pass
            # raise ValueError("Year cannot be below 1900")
        else:
            self.__year = new_year

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director):
        self.__director = new_director

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if runtime < 1:
            raise ValueError("Runtime must be positive")
        else:
            self.__runtime_minutes = runtime

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors_list):
        if type(actors_list) is list:
            self.__actors = actors_list

    def add_actor(self, new_actor: Actor):
        if type(new_actor) is Actor:
            self.__actors.append(new_actor)

    def remove_actor(self, del_actor: Actor):
        try:
            index = self.__actors.index(del_actor)
        except ValueError:
            pass
        else:
            self.__actors.pop(index)

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres_list):
        if type(genres_list) is list:
            self.__genres = genres_list

    def add_genre(self, genre: Genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        try:
            index = self.__genres.index(genre)
        except ValueError:
            pass
        else:
            self.__genres.pop(index)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc: str):
        if type(desc) is str:
            self.__description = desc.strip()

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if self.__title == other.title and self.__year == other.year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.title:
            if self.__year < other.year:
                return True
            else:
                return False
        elif self.__title < other.title:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__title + str(self.__year))


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) is Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) is str:
            self.__review_text = review_text.strip()
        else:
            self.__review_text = ""

        if 11 > rating > 0 and type(rating) is int:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie} Rating: {self.__rating}>"

    def __eq__(self, other):
        if self.__movie == other.movie and self.__rating == other.rating and self.__review_text == other.review_text and self.__timestamp == other.timestamp:
            return True
        else:
            return False


class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name.lower().strip()
        self.__password = password

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        self.__reviews.append(review)

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__user_name < other.user_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__user_name)


class WatchList:
    def __init__(self):
        self.__watch_list = []

    @property
    def watch_list(self):
        return self.__watch_list

    def add_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        try:
            index = self.__watch_list.index(movie)
        except ValueError:
            pass
        else:
            self.__watch_list.pop(index)

    def select_movie_to_watch(self, index):
        if index >= len(self.__watch_list):
            # print("NONE RETURN")
            return None
        else:
            # print("RETURN MOVIE")
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        return self.select_movie_to_watch(0)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.size():
            result = self.select_movie_to_watch(self.n)
            self.n += 1
            return result
        else:
            raise StopIteration


class Ranking:
    def __init__(self, watchlist_list=None):
        self.__ranking = dict()

        if isinstance(watchlist_list, list):
            for sub_watchlist in watchlist_list:
                for movie in sub_watchlist.watch_list:
                    try:
                        self.__ranking[movie.__repr__()] += 1
                    except:
                        self.__ranking[movie.__repr__()] = 1

    @property
    def ranking(self):
        return self.__ranking

    def import_watch_list(self, watch_list_in: WatchList):
        for movie in watch_list_in.watch_list:
            try:
                self.__ranking[movie.__repr__()] += 1
            except:
                self.__ranking[movie.__repr__()] = 1

    def import_multi_watch_list(self, watchlist_list=None):
        if isinstance(watchlist_list, list):
            for sub_watchlist in watchlist_list:
                for movie in sub_watchlist.watch_list:
                    try:
                        self.__ranking[movie.__repr__()] += 1
                    except:
                        self.__ranking[movie.__repr__()] = 1

    def most_watched(self, rows=10):
        sorted_ranking = sorted(self.__ranking.items(), key=lambda x: x[1], reverse=True)

        r_list = []
        x = 0
        for mv in sorted_ranking:
            if x < rows:
                # print(mv[0], mv[1])
                r_list.append(f"{x}: {mv[0]} Count {mv[1]}")
            else:
                return r_list

            x += 1

        return r_list
