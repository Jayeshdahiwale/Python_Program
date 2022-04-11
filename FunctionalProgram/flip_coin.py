"""

@Author: Jayesh Dahiwale
@Date: 2022-04-11 20:49:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-11 18:00:30
@Title : Flip_Coin

"""
import random

"""
This function takes the no of flips as input and output the percentage of head and tails
"""


def flip_coin():
    no_of_flips = int(input("Enter the number of times you want to flip coin :"))
    if no_of_flips < 0:
        print('Enter the positive value')
        return flip_coin()
    head = 0
    tail = 0
    for flip in range(no_of_flips):
        rand_num = random.uniform(0, 1)
        if rand_num < 0.5:
            tail += 1
        else:
            head += 1
    print(f"Percentage of heads :{round((head / (head + tail)) * 100, 2)}%")
    print(f"Percentage of tails :{round((tail / (head + tail)) * 100, 2)}%")


flip_coin()
