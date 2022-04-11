"""

@Author: Jayesh Dahiwale
@Date: 2022-04-11 21:45:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-11 22:00:00
@Title : Harmonic Number

"""


def harmonic_number():
    number = int(input("Enter the non zero positive number to get harmonic sum :"))
    if number <= 0:
        print("Enter the non-zero positive integer")
        return harmonic_number()
    harmonic_sum = 0
    for i in range(1, number + 1):
        harmonic_sum += 1 / i
    print(f"The harmonic sum is :{harmonic_sum}")


harmonic_number()
