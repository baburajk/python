#!/usr/local/bin/python3
import sys
import argparse

class BSearch(object):
	""" Class created for testing Binary Search programs"""

	def findnum(self,target,nlist):
		""" Check if the target exists in the list """

		floor = -1
		ceil = len(nlist)

		while floor + 1 < ceil:
			print ( "Floor , Ceil", floor, ceil )
			dist = ceil - floor
			half = int(dist / 2)
			gind = floor + half
			print ( "Index is now", gind)

			gval = nlist[gind]

			if gval == target:
				print ("gval = target ", gval, target )
				return True

			if gval > target:
				#Target is on the left, move the ceil to left
				print ("gval > target", gval, target )
				print ("Target is to the left, move ceil to left: ceil = gind ",ceil,gind)
				ceil = gind
			else:
				#Target is to the right, move floor to right
				print ("gval < target", gval, target )
				print ("Target is to the right , move floor to right : floor = gind ",floor,gind)
				floor = gind

		#while

		return False
	#def 


def main():
	bsearch  = BSearch()

	cli = argparse.ArgumentParser()
	cli.add_argument("--list",nargs="*",type=int,default=[1,2,3,4])
	cli.add_argument("--target",type=int)
	args = cli.parse_args()

	print ("List : ", args.list)
	print ("Target: ", args.target)

	#nlist = [1,2,3,4,5,6,7]
	#print ("Input: ", nlist )
	#bsearch.findnum(6,nlist)
	bsearch.findnum(args.target, args.list)

if __name__ == "__main__":
	main()

#BSearch
