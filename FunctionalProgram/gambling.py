"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 07:31:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 22:00:00
@Title : Gambling

"""
import random

"""
This function is tells whether the player will win or lose and the percentage of win and loss
"""


def gambling():
    inputs = [int(i) for i in input("Enter the stake,bet,goal separate by comma :").split(",")]
    no_of_wins = 0
    no_of_loss = 0

    stake = inputs[0]
    bet = inputs[1]
    goal = inputs[2]
    while stake >= bet:
        result = random.randint(0, 1)
        if result == 0:
            stake -= bet
            no_of_loss += 1
        else:
            stake += bet
            no_of_wins += 1
        if stake >= goal:
            print("Goal achieved")
            break
        elif stake < bet:
            print("Gambler turns out to be bancrupt")
            break
    print(f"Total no of wins {no_of_wins} & Total no of loss {no_of_loss}")
    print(
        f"Percentage of win :{round(no_of_wins * 100 / (no_of_wins + no_of_loss), 2)}% ,Percentage of loss :{round(no_of_loss * 100 / (no_of_wins + no_of_loss), 2)}%")


gambling()
