# Justin Williams
# Assignment 02
# EPD 455: Python for Applications in Engineering
# 2022-09-25
#
# Problem 5:
# Write a function middle(a) that takes a list a and returns a new list that 
# contains all but the first and last elements. Submit the python script as 
# task5.py on Canvas.
# Note: This function does not take command line arguments but will rather be 
# imported into another python script and called from there.
#

# listy = [1,7,"up", -5.9, "youwanttogokayaking",3]

def middle(a):
    new_list = a[1:-1]
    return new_list

# print(middle(listy))
