

def is_a_palindrome(string):

	#Track the characters
	track = set()

	for char in string:
		if char in track:
			track.remove(char)
		else:
			track.add(char)

	print (string, len(track) ,track)


is_a_palindrome("civic")
is_a_palindrome("ivicc")
is_a_palindrome("civil")
is_a_palindrome("livci")

