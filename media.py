import webbrowser

class Movie():
	""" This class stores movie related information, including the movie title, 
		an image of the movie poster and the movie trailer. """

	def __init__(self, movie_title, poster_image, youtube_trailer):
		self.title = movie_title                     
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

	def show_trailer(self):
		""" This function will open the movie trailer url in the default 
		browser.
		"""
		webbrowser.open(self.trailer_youtube_url)
 
