#!/usr/local/bin/python3


class Flight:

	def movie_lengths(self, flight_length):
		movie_length_list = [5, 3, 2, 4, 1 ,9 ]
		print (movie_length_list)

		movies_seen = set()

		#Loop through the list
		for first_movie in movie_length_list:
			second_movie = flight_length - first_movie
			print ("Second movie", second_movie )
			if second_movie in movies_seen:
				print ("Movies Seen ", movies_seen)
				return True
			print ("Adding to movies seen", first_movie)
			movies_seen.add(first_movie)

	#def


flight = Flight()
flight.movie_lengths(8)

#Flight


