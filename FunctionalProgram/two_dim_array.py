"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 08:19:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 22:00:00
@Title : Two Dimensional Array

"""


def two_dim_array():
    inputs = [int(i) for i in input("Enter the no of rows , columns separate by comma :").split(",")]
    elements = input("Enter the (rows X cols) elements separated by comma :").split(",")
    rows = inputs[0]
    cols = inputs[1]
    two_d_array = []
    for i in range(rows):
        one_d_array = []
        for j in range(cols):
            one_d_array.append(elements[i*cols+j])
        two_d_array.append(one_d_array)
    print(two_d_array)
two_dim_array()