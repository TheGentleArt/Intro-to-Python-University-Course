# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-03
#
# =============================================================================
# Problem 02
# 
# Generate a list heightsM of random floats between 1.5 and 2.2. Think of these numbers as
# heights in metres. The list should have 20 entries. Ensure that the floats stored in the list
# heights has a maximum of 2 decimal places.
# Create a new list heightsFt that takes all the elements in heightsM and converts them into
# heights in feet and inches. Foe example, 1.85 in heightsM will be converted to 6’0” in heightsFt.
# Notice that the feet and inches are rounded of to the lower integer in heightsFt.
# Print the first and last element of hieghtsM followed by the first and last element of heightsFt
# in a new line (see sample output below). Use 1 inch = 0.0254 metres
# =============================================================================
# 
#
import math
from random import randint

num_digits = 2 # number of digits after decimal point
num_points = 20 # length of list, given in problem statement
lim_lower = 1.5 # given in problem statement
lim_upper = 2.2 # given in problem statement


heightsM = [ randint(lim_lower*10,lim_upper*10)/10 for i in range(0,num_points) ]

heightsFt_ftonly = [ math.floor(heightsM[i]*(100/2.54)/12) for i in range(len(heightsM)) ]
heightsFt_inchesonly = [ math.floor(heightsM[i]*(100/2.54)%12) for i in range(len(heightsM)) ]
heightsFt = [str(heightsFt_ftonly[i])+"' "+str(heightsFt_inchesonly[i])+' " ' for i in range(len(heightsM))]

print("The first and last values of heightsM: ",heightsM[0]," ",heightsM[-1])
print("The first and last values of heightsFt: ",heightsFt[0]," ",heightsFt[-1])
