#!/usr/local/bin/python3

import argparse


class OrderMerge:
        pass

        def merge(self,list1,list2):
                # Make a list to hold both lists
                mergedlistsize = len(list1) + len(list2)
                mergedlist = [None] * mergedlistsize

                current_index_list1 = 0
                current_index_list2 = 0
                current_index_merged  = 0

                while current_index_merged < mergedlistsize:
                        #Get value from first list1 and list2
                        if current_index_list1 < len(list1):
                                first_unmerged_list1 = list1[current_index_list1]
                        if current_index_list2 < len(list2):
                                first_unmerged_list2 = list2[current_index_list2]

                        if first_unmerged_list1 < first_unmerged_list2:
                                mergedlist[current_index_merged] = first_unmerged_list1
                                current_index_list1 = current_index_list1 + 1
                        else:
                                mergedlist[current_index_merged] = first_unmerged_list2
                                current_index_list2 = current_index_list2 + 1

                        current_index_merged = current_index_merged + 1

                return mergedlist
        #def


#OrderMerge


def main():
        cli = argparse.ArgumentParser()
        cli.add_argument("--list1",nargs="*",type=int)
        cli.add_argument("--list2",nargs="*",type=int)
        args = cli.parse_args()

        print ("List1", args.list1)
        print ("List2", args.list2)

        omerge = OrderMerge()
        result = omerge.merge(args.list1, args.list2)
        print ("Result:" , result)

if __name__ == "__main__":
        main()



