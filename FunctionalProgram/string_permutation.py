"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 11:22:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 22:00:00
@Title : Distance Calculater

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")
""" Below function is used to swap the characters in a character list"""


def swap(A, i, j):
    c = A[i]
    A[i] = A[j]
    A[j] = c


"""Below function is used to reverse a list between specified indexes"""


def reverse(A, i, j):
    # do till two endpoints intersect
    while i < j:
        swap(A, i, j)
        i = i + 1
        j = j - 1


"""Iterative function to find permutations of a string in Python"""


def permutations(s):
    # base case
    if not s:
        return []

    # base case
    if len(s) == 1:
        return [s]

    n = len(s)

    # sort the string in a natural order
    chars = sorted(list(s))

    while True:

        # print the current permutation
        print(''.join(chars), end=' ')
        logging.info(''.join(chars))

        i = n - 1
        while chars[i - 1] >= chars[i]:

            i = i - 1
            if i == 0:
                return

        j = n - 1
        while j > i and chars[j] <= chars[i - 1]:
            j = j - 1

        swap(chars, i - 1, j)

        reverse(chars, i, n - 1)


if __name__ == '__main__':
    s = input("Enter the string :")
    permutations(s)
