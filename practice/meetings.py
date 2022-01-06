#!/usr/local/bin/python3

import argparse

def merge(meetings):

	#Sort the meetings (n log n)
	sorted_meetings = sorted(meetings)

	#Save the first entry, without the square brackets the return will be a tupe (element), instead of the list!!
	merged_meetings = [sorted_meetings[0]]

	#Loop from the second element
	for current_meeting_start,current_meeting_end in sorted_meetings[1:]:
		last_meeting_in_merged_start, last_meeting_in_merged_end = merged_meetings[-1]

		if last_meeting_in_merged_start <= current_meeting_end and last_meeting_in_merged_end <= current_meeting_start:
			merged_meetings[-1] = (last_meeting_in_merged_start, current_meeting_end)
		else:
			merged_meetings.append((current_meeting_start, current_meeting_end))

	print ("Unsorted", meetings )
	print ("Sorted", sorted_meetings)
	print ("Merged", merged_meetings)

#def

meetings = [(10, 12), (4, 8), (0, 1), (9, 10), (3, 5) ]
merge (meetings)

