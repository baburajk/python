#!/usr/local/bin/python3
""" Module to hold the string specific algorithms """

__author__ = 'Author Name here'

import sys
import os

class MyString(object):
    """Generic class to hold the methods specific to string related operations..."""

    def findLengthOfLongestSubstr(self,instr):
        """ Length of the longest substring with non repeating characters """

        slen = len(instr)
        if slen < 2:
            return "User Error: String should have at least two chars!!!"
        else:
            counter = 1           #Since count is done while comparing two elements, start with 1
            mylist = list(instr)  #Convert the string to a stack, to pop elements out
            marker = mylist.pop() #Need a marker for comparison to the adjacent element.
            strlen = 0
            while mylist:
                curr =  mylist.pop()
                if curr != marker:
                    counter = counter + 1
                if curr == marker or not mylist: 
                    if counter > 1:              #Discovered at least one 'nrc' sequence occurence.
                        strlen = max (strlen, counter)
                    counter = 1                  #Counter reset for subsequent nrc searches
                marker = curr

        return strlen
    #def

def main():
    demo = MyString()
    instr = sys.argv[1]
    print ("Input : " , instr )
    result = demo.findLengthOfLongestSubstr(instr)
    print("Output:" , result)

if __name__ == "__main__":
    main()


