"""This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.

Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

Try invoking your function with the input “Black Panther”.

HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache."""

import requests_with_caching
import json
def get_movies_from_tastedive(s):
    d={'q':s,'type':'movies','limit':5}
    resp=requests_with_caching.get("https://tastedive.com/api/similar",params=d)
    #print(resp)
    #print(resp.url)
    response_d=resp.json()
    return response_d
#get_movies_from_tastedive("Bridesmaids")
#get_movies_from_tastedive("Black Panther")
def extract_movie_titles(d):
    name=[]
    x=d['Similar']
    y=x['Results']
    for i in y:
        name.append(i['Name'])
    #print(name)
    return name
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def get_related_titles(l):
    f=[]
    o=[]
    for i in l:
        f=extract_movie_titles(get_movies_from_tastedive(i))
        for j in f:
                o.append(j)
        #print(list(set(o)))
    return list(set(o))
#get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

def get_movie_data(movieName):
    d={'t':movieName,'r':'json'}
    resp=requests_with_caching.get("http://www.omdbapi.com/",params=d)
    print(resp.url)
    respDic = resp.json()
    return respDic
#get_movie_data("Venom")
#get_movie_data("Baby Mama")

def get_movie_rating(d):
    rate=d['Ratings']
    for i in rate:
        if i['Source'] == 'Rotten Tomatoes':
                #print(int(i['Value'][:-1]))
                return int(i['Value'][:-1])
    return 0
#get_movie_rating(get_movie_data("Venom"))
#get_movie_rating(get_movie_data("Deadpool 2"))

def get_sorted_recommendations(l):
    new_l=get_related_titles(l)
    dict={}
    for i in new_l:
        dict[i]=get_movie_rating(get_movie_data(i))
    print(dict)
    return [i[0] for i in sorted(dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]