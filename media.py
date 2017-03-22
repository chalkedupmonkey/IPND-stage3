import webbrowser

class Video():

    """
        Highest level class, contains all universal attributes
        for any current or future class movies, tv shows, etc.
        Dot operator allows future classes to instantiate categories.
    """


    def __init__(self, title, release_year, rating, runtime, genre, rt_score, review, poster_image_url, trailer_youtube_url):

        self.title = title
        self.year = release_year
        self.rating = rating
        self.runtime = runtime
        self.genre = genre
        self.score = rt_score
        self.review = review
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Video):

    """
        Retreives info from Videos if in same category for movies.
        Currently no categories that differ.
    """

    MPAA = ['NR', 'G', 'PG', 'PG-13', 'R', 'NC-17']

    def __init__(self, title, release_year, rating, runtime, genre, rt_score, review, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, release_year, rating, runtime, genre, rt_score, review, poster_image_url, trailer_youtube_url)



#    def show_trailer(self):
#        webbrowser.open(self.trailer_youtube_url)



#class Anime(Video):
#
#   """ Class for anime. Currently having a hard time thinking of anime. """
#


#    def __init__(self, title, release_year, rating, runtime, genre, rt_score, review, poster_image_url, trailer_youtube_url):
#        Video.__init__(self, title, release_year, rating, runtime, genre, rt_score, review, poster_image_url, trailer_youtube_url)


# class TVShow(Video):
#
#   """ Class for TV Shows. Currently having a hard time thinking of tv shows. """
#
#
#    VCHIP = ['TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-PG14', 'TV-MA']
#
#    def __init__(self, title, release_year, rating, runtime, genre, rt_score, poster_image_url, trailer_youtube_url):
#        Video.__init__(self, title, release_year, rating, runtime, genre, rt_score, poster_image_url, trailer_youtube_url)
