"""
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
""" 

import pandas as pd
from bs4 import BeautifulSoup 
import requests
## defining the function
def imdb_id(id_number):
    r = requests.get("http://www.imdb.com/title/" + id_number)
    b = BeautifulSoup(r.text)
    # List of ratings. I found this was easier than trying to pick out the 
    # the actual movie rating from the text of the movie rating sentence    
    ratings = ["NC-17", "R", "PG-13", "PG", "G", "NR", "Unrated", "Not Rated", "TV-Y", "TV-Y7", "TV-G", "TV-PG", "TV-14", "TV-MA"]
    
    #Extracting the Movie Title    
    title = b.find_all(name="span", attrs={"itemprop":"name"})[0].text
    # Extracting the star rating
    star_rating = b.find_all(name="span", attrs={"itemprop":"ratingValue"})[0].text
    # Extracting the Description
    description = b.find_all(name="p", attrs={"itemprop":"description"})[0].text
    #getting the intial content rating field from the imported data
    content_rating = b.find_all(name="span", attrs={"itemprop":"contentRating"})[0].text
    # Created a function to search the found "content field" for the movie rating.
    # because the field wasn't just the rating itself. It was more complicated
    # like "for fantasy violence. So this function will check the rating list
    # against the pulled in content rating sentence from the web 
    def final_content_rating():
        for i in range(len(ratings)):
            if ratings[i] in content_rating:
                return(ratings[i])
    
    #storing the result of the final content rating function        
    scrubbed_content_rating = final_content_rating()
    
    #Getting the movie duration
    duration = b.find_all(name="time", attrs={"itemprop":"duration"})[0].text.strip()
    #a combined dictionary to be easily returned from the function.
    results = {"title":title, "star_rating":star_rating, "description": description, "content_rating":scrubbed_content_rating, "duration":duration}
    return(results)

# importing the file with the test IMDB movie IDs and turned them into a list
# to feed into the IMDB function above
with open('imdb_ids.txt') as f:
    test_imdb_ids = []
    for row in f:
        test_imdb_ids.append(row)

# Creating a list of dictionaries of the passed in IMDB movie ids.  

final_list = []
for imdb in test_imdb_ids:
    x = imdb_id(imdb)
    final_list.append(x)

# converting the list of diciontaries into a Pandas data frame

final_list_of_movies  = pd.DataFrame(final_list)