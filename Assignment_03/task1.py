# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-03
#
# =============================================================================
# # Problem 01
# #
# # The purpose of this problem is to assess how various ways of processing lists compare in terms
# # of efficiency.
# # (a) Generate a list A of random floats, between -1.0 and 1.0. It should have 1,000,000 entries.
# # See here on how to generate random numbers in python.
# # (b) Use list comprehensions to generate another list that takes every other entry in A, from
# # end to beginning, and squares it. This would be list B (half the length of A).
# # (c) Just bullet (1b) above, but instead use now a for-loop for the same list A to get list C
# # (should be identical to B).
# # (d) Just bullet (1b) above, but instead use now a while-loop to get list D.
# # (e) Using process time, assess how much time in seconds it takes to get B,C, and D.
# # (f) Print the time taken to generate B, the first element of B and the last element of B. Do the
# # same for the for-loop and while-loop (see sample output below).
# =============================================================================
#
import random
from random import randint
# import matplotlib.pyplot as plt
import time


num_digits = 3 # number of digits after decimal point
num_points = 1000000#1000000 # length of list, given in problem statement
lim_lower = -1 # given in problem statement
lim_upper = 1 # given in problem statement

# Generating list A
A = []
for points in range(num_points):
    A.append(randint(-10**num_digits,10**num_digits)/(10**num_digits))
             
# # Below was used with fewwer points (5000) to test with
# listy = list(range(0,num_points))
# plt.figure()
# plt.scatter(listy, A, c='blue', s=1)

# Generating list B
tic = time.process_time()
B = [ A[i]**2 for i in range(0,len(A)) if (i % 2 == 0) ]
toc = time.process_time()
tictoc_B = toc-tic
print("Time to get B was: ", tictoc_B)
print("The first element of B was: ", B[0])
print("The last element of B was: ", B[-1],"\n")

# Generating list C
tic = time.process_time()
C = []
for number in range(0,len(A)):
    if number % 2 == 0:
        C.append(A[number]**2)
toc = time.process_time()
tictoc_C = toc-tic
print("Time to get C was: ", tictoc_C)
print("The first element of C was: ", C[0])
print("The last element of C was: ", C[-1],"\n")

# Generating list D
tic = time.process_time()
D = []
i = 0
while i < len(A):
    if i % 2 == 0:
        D.append(A[i]**2)
    i += 1
toc = time.process_time()
tictoc_D = toc-tic

# Print information to terminal
print("Time to get D was: ", tictoc_D)
print("The first element of D was: ", D[0])
print("The last element of D was: ", D[-1],"\n")
print("Time for C was ",round((tictoc_C/tictoc_B-1)*100,2),"% more time than B.")
print("Time for D was ",round((tictoc_D/tictoc_B-1)*100,2),"% more time than B.\n")   
