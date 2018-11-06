#!/usr/local/bin/python3
import argparse

class MergeSort:
	""" Merge sort example """

	def mergesort(self,unsortedlist):
		
		if len(unsortedlist) < 2:
			return unsortedlist	

		#Step:1 Divide list in half
		midindex = int(len(unsortedlist) / 2) 
		unsortedleft = unsortedlist[:midindex]
		unsortedright = unsortedlist[midindex:]
		
		print ("Recursion", unsortedleft, unsortedright)
		#Step:2 Sort each half
		sortedleft = self.mergesort(unsortedleft)
		print ("Sorted Left" , sortedleft)
		sortedright = self.mergesort(unsortedright)
		print ("Sorted Right" , sortedright)

		#Step:3 Merge each halves
		sortedlist = []
		while len(sortedlist) < len(unsortedlist):
			#unsortedleft's first element comes next if it's less than 
			#Unsorted rights first element or if unsortedright is empty

			print ("Inside loop", sortedleft, sortedright)
			if sortedleft and ((not sortedright)  or sortedleft[0] < sortedright[0]):
				sortedlist.append(sortedleft.pop(0))
			else:
				sortedlist.append(sortedright.pop(0))
			print ("Sorted list", sortedlist, sortedleft,sortedright)

		return sortedlist
	#mergesort

def main():
	cli = argparse.ArgumentParser()
	cli.add_argument("--list",nargs="*",type=int,default=[1,2,3,4])
	args = cli.parse_args()
	msort = MergeSort()
	msort.mergesort(args.list)

if __name__ == "__main__":
	main()

#MergeSort
