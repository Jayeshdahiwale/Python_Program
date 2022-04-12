"""

@Author: Jayesh Dahiwale
@Date: 2022-04-11 20:25:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-11 18:00:30
@Title : UserName

"""

"""
Below function asks for the username and greet with the username
"""


def user_name():
    name = input("Enter the name :")
    if len(name) >= 3:
        print(f"Hello {name}, how are you ?")


user_name()
