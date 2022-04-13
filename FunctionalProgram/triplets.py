"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 08:44:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 22:00:00
@Title : Triplets(Returning Zero Sum)

"""

""" This function returns the set of triplets such that its elements return zero sum"""


def triplets():
    no_of_integer = int(input("Enter no of integers :"))
    integers_array = [int(i) for i in input("enter the integers separated by commas :").split(",")]
    triplet_set = []
    for i in range(no_of_integer - 2):
        for j in range(i+1, no_of_integer - 1):
            for k in range(j+1, no_of_integer):
                if integers_array[i] + integers_array[j] + integers_array[k] == 0:
                    triplet_set.append([integers_array[i], integers_array[j], integers_array[k]])
    print(triplet_set)


triplets()
