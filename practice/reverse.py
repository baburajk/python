#!/usr/local/bin/python3

import sys
import argparse


class Reverse:

	def reverse_chars(self,message,start,end):
		left_index = start
		right_index = end

		while left_index < right_index:
			message[left_index], message[right_index] = message[right_index], message[left_index]
			left_index = left_index + 1
			right_index = right_index - 1

		return message
	#def

	def reverse_word(self,message):
		start_index = 0
		for i in range (len(message) ):
			if (message[i] == ' '):
				self.reverse_chars(message, start_index, i - 1)
				start_index = i + 1
			elif (i == len(message) -1 ):
				self.reverse_chars(message, start_index, i )
		return message
	#def


def main():
	mylist=[ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ]
	print ("Input", mylist)
	mobj = Reverse()
	result = mobj.reverse_chars(mylist,0, len(mylist) - 1 )
	print("Reversed Characters", result)
	final = mobj.reverse_word(result)
	print("Reversed Words", final )

#def

if __name__ == "__main__":
	main()

