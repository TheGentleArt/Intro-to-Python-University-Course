# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-03
#
# =============================================================================
# Problem 03
# 
# Write a python script task3.py with the following functions:
# (a) A function dataGen(n,a,b,fileName) that takes as input 3 integers a, b and n and writes
# to a file given by fileName (provided with the extension) in the current working directory
# with n random integers between a and b. Each number in the file should be seperated by
# a space.
# (b) A function dataRead(fileName), that reads the values in the file given by fileName and
# returns a list of the values.
# (c) A function sumFile(fileName1,fileName2,k) that takes as input two filenames fileName1
# and fileName2 and an integer k, and finds all u and v such that u + v = k where u is an
# element of the first file and v is a member of the second file. The function should return a
# list with each element of the list as a tuple of the u,v pairs. The output below shows the
# list of numbers obtained from the two files and all the pairs that add up to k=4.
# [3 , 3 , 3 , 3 , 1 , 1 , 1 , 4 , 4 , 3]
# [2 , 1 , 2 , 4 , 2 , 4 , 2 , 1 , 3 , 2]
# [(3 , 1) , (3 , 1) , (3 , 1) , (3 , 1) , (1 , 3) , (1 , 3) , (1 , 3) , (3 , 1)]
# =============================================================================
#

from random import randint

def dataGen(n,a,b,fileName):
    values = [ randint(a,b) for i in range(0,n)]
    with open(fileName, "x") as file:
        file.write(str(values))
# testing above code:  
dataGen(10,1,4,"randofile1.txt")
dataGen(10,-10,10,"randofile2.txt")

def dataRead(fileName):
    with open(fileName, "r") as file:
        for item in file:
            return item
# testing above code:
print("randoFile1 contents: \n",dataRead("randofile1.txt"),"\n")
print("randoFile1 contents: \n",dataRead("randofile2.txt"),"\n")

def sumFile(fileName1, fileName2, k):
    with open(fileName1, "r") as file1, open(fileName2, "r") as file2:
        for items in file1:
            file_contents_1 = items
            return file_contents_1
        for items in file2:
            file_contents_2 = items
# Still need to finish this up...
        
