#!/usr/local/bin/python3


class Word:

	def split_words(split,instring):
		words = []
		word_length = 0

		for index, char in enumerate(instring):
			if char.isalpha():
				if word_length == 0:
					start_index = index
				word_length = word_length + 1
			else:
				word = instring[start_index:start_index + word_length]
				word_length = 0
				words.append(word)
		#for
		print (words)
		return words

	#def


	def word_count(self,words):

		words_to_counts = {}

		for word in words:
			if word in words_to_counts:
				words_to_counts[word] += 1
			else:
				words_to_counts[word] = 1

		print (words_to_counts)

	#def

#Word

word = Word()
result = word.split_words("Jack and Jill went up the hill, Jack fell down and Jill came tumbling after")

word.word_count(result)

