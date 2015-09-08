'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies

movies = pd.read_csv("c:\Users\Ben\Documents\DAT8\data\imdb_1000.csv")

# check the number of rows and columns

movies.shape

# check the data type of each column

movies.dtypes

# calculate the average movie duration

movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies

movies.sort("duration").head(1)
movies.sort("duration").tail(1)

# create a histogram of duration, choosing an "appropriate" number of bins

movies.duration.plot(kind='hist', bins=11)

# use a box plot to display that same data

movies.duration.plot(kind='box')
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings

movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels

movies.content_rating.value_counts().plot(kind='bar', title='Number of Movies in Each Ratings Category')
plt.xlabel("Rating")
plt.ylabel("Number of Movies in Each Rating")

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
[if variable == "NOT RATED" or "APPROVED" or "PASSED" or "GP"]

#I realized i could just do the replace method 4 times but my programming
# efficiency would not let me do it and I wasn't able to find a more elegant 
# way
# convert the following content ratings to "NC-17": X, TV-MA
?
# count the number of missing values in each 
?

# if there are missing values: examine them, then fill them in with "reasonable" values
?
# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
?

above_two_hours = movies[movies.duration > 120].star_rating.mean()
below_two_hours = movies[movies.duration < 120].star_rating.mean()
print above_two_hours, below_two_hours

# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind="scatter", x="duration", y="star_rating", alpha=0.3)

# calculate the average duration for each genre

print movies[movies.genre == False]

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.plot(kind='scatter', x='duration', y='content_rating')

# determine the top rated movie (by star rating) for each genre
## I couldn't finish these

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
