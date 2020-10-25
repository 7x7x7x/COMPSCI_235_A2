import csv
import os
import random

from movie.domain.model import *
from movie.adapters.repository_interface import *
from werkzeug.security import generate_password_hash


# need to implement password hash


class RepositoryMemory(RepositoryInterface):

    def __init__(self):
        self.__users = []
        self.__movies = []
        self.__actors = []
        self.__directors = []
        self.__genres = []
        self.__reviews = {}
        self.__view_count = {}
        self.__trailer_id = {}

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, username) -> User:
        print("Check " + username)
        for user in self.__users:
            print("comp: " + user.user_name)
            if user.user_name == username:
                print("hash: " + user.password)
                return user
        return None

    def movie_filter_actor(self, actor: Actor):
        r_list = []

        if actor in self.__actors:
            for mv in self.__movies:
                if actor in mv.actors:
                    r_list.append(mv)

        return r_list

    # fixed director search
    def movie_filter_director(self, director: Director):
        r_list = []

        if director in self.__directors:
            for mv in self.__movies:
                if director == mv.director:
                    r_list.append(mv)

        return r_list

    def movie_filter_genre(self, genre: Genre):
        r_list = []

        if genre in self.__actors:
            for mv in self.__movies:
                if genre in mv.genres:
                    r_list.append(mv)

        return r_list

    def movie_random(self, number: int):
        # temp solution
        r_list = []
        selection = random.sample(range(len(self.__movies)), number)
        for index in selection:
            r_list.append(self.__movies[index])
        return r_list

    # memory repo functions
    def add_movie(self, movie: Movie):
        self.__movies.append(movie)

    def add_user(self, user: User):
        self.__users.append(user)

    def movie_filter_year(self, year: int):
        r_list = []
        for mv in self.__movies:
            # print(mv)
            if mv.year == year:
                # print(mv.title + " added")
                r_list.append(mv)

        return r_list

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def add_director(self, director: Director):
        self.__directors.append(director)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def get_movie_list(self):
        return self.__movies

    def get_genre_list(self):
        return self.__genres

    def get_actor_list(self):
        return self.__actors

    def get_director_list(self):
        return self.__directors

    def add_review(self, movie: str, review: str):
        try:
            self.__reviews[movie].append(review)
        except KeyError:
            self.__reviews[movie] = [review]

    def get_review(self, movie: str):
        try:
            r = self.__reviews[movie]
            return r
        except KeyError:
            r = []
            return r

    def add_view(self, movie: str, quantity: int):
        try:
            self.__view_count[movie] += quantity
        except KeyError:
            self.__view_count[movie] = quantity

    def view_count(self, movie: str):
        if movie is None:
            return self.__view_count
        else:
            r = 0
            try:
                r = self.__view_count[movie]
                return r
            except KeyError:
                return r

    def add_trailer(self, movie: str, yt_id: str):
        self.__trailer_id[movie] = yt_id

    def get_trailer(self, movie: str):
        if movie in self.__trailer_id:
            return self.__trailer_id[movie]
        else:
            # placeholder url
            return "3cYBfuphkuE"


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: str, repo: RepositoryMemory):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def load_trailers(data_path: str, repo: RepositoryMemory):
    trailers = {}

    for data_row in read_csv_file(os.path.join(data_path, 'trailers.csv')):
        repo.add_trailer(data_row[0], data_row[1])


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                description = row['Description']

                self.__dataset_of_movies.append(Movie(title, release_year))
                self.__dataset_of_movies[-1].description = description
                # print(f"Movie {index} with title: {title}, release year {release_year}")

                actors = row['Actors'].split(',')
                temp_director = Director(row['Director'])
                genres = row['Genre'].split(',')

                for a in actors:
                    temp_actor = Actor(a.strip())

                    # add actor to current movie
                    self.__dataset_of_movies[-1].add_actor(temp_actor)

                    if temp_actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(temp_actor)

                # add director to current movie
                self.__dataset_of_movies[-1].director = temp_director

                if temp_director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(temp_director)

                for g in genres:
                    temp_genre = Genre(g.strip())

                    # add genre to current movie
                    self.__dataset_of_movies[-1].add_genre(temp_genre)

                    if temp_genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(temp_genre)

                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors
