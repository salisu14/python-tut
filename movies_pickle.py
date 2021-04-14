#!/usr/bin/env python3

import pickle

movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1956],
          ["On the Waterfront", 1954]]

with open('movies.txt', 'wb') as file:
    pickle.dump(movies, file)


with open('movies.txt', 'rb') as readfile:
    movies = pickle.load(readfile)
    print(movies)