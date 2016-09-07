import media
import fresh_tomatoes

# Create object Alice in Wonderland
alice_in_wonderland = media.Movie("Alice in Wonderland", 
								  "http://ia.media-imdb.com/images/M/MV5BMTMwNjAxMTc0Nl5BMl5BanBnXkFtZTcwODc3ODk5Mg@@._V1_SX300.jpg",  # NOQA 
						          "https://www.youtube.com/watch?v=9POCgSRVvf0")


# Create object WALL-E
wall_e = media.Movie("WALL-E",
				     "http://ia.media-imdb.com/images/M/MV5BMTczOTA3MzY2N15BMl5BanBnXkFtZTcwOTYwNjE2MQ@@._V1_SX300.jpg",  # NOQA
				     "https://www.youtube.com/watch?v=alIq_wG9FNk")


# Create object Jungle Book
jungle_book = media.Movie("The Jungle Book",
						  "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh",  # NOQA
						  "https://www.youtube.com/watch?v=5mkm22yO-bs")


# Create object Shrek
shrek = media.Movie("Shrek",
					"http://ia.media-imdb.com/images/M/MV5BMTk2NTE1NTE0M15BMl5BanBnXkFtZTgwNjY4NTYxMTE@._V1_SX300.jpg",  # NOQA
					"https://www.youtube.com/watch?v=ooJJX3R42WM")

# Create object Up
up = media.Movie("Up",
				 "https://projectedrealities.files.wordpress.com/2014/01/up_poster1500.jpg", # NOQA
				 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

# Create object Ice Age
ice_age = media.Movie("Ice Age",
					  "http://i2.listal.com/image/712085/600full-ice-age-poster.jpg",  # NOQA
					  "https://www.youtube.com/watch?v=2euZ_BfJH8I")

# List of movies
movies = [alice_in_wonderland, wall_e, jungle_book, shrek, up, ice_age]

# Open website that shows movies in list
fresh_tomatoes.open_movies_page(movies)


