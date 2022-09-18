# Justin Williams
# EPD 455: Python for Applications in Engineering
# Assignment 01
# 2022-09-17
#
# Problems statement for problem # 6 on homework:
#
# Write a python program that computes the 2D distance between two points given
# their x and y coordinates. The program takes 4 floats (coordinatesx1,y1,x2,
# and y2) as input from the command line and prints the distance between the 
# two points as the output. The python file should be named task6.py and 
# uploaded to Canvas. Hint: If you are having trouble reading inputs from the
# command line, look into sys module python.
#

x_1 = float(input('Enter x1 value: '))
y_1 = float(input('Enter y1 value: '))

x_2 = float(input('\nEnter x2 value: '))
y_2 = float(input('Enter y2 value: '))

print("\nCalculating distance between the two points...")
delta_x = x_2 - x_1
delta_y = y_2 - y_1

dist = (delta_x**2 + delta_y**2)**(1/2)
print('Distance is: ',dist)
