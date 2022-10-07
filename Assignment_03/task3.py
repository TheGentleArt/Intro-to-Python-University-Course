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

# from random import randint
import numpy as np



def dataGen(n,a,b,fileName):
    values = np.random.randint(a, b, size=n)
    #values = [ randint(a,b) for i in range(0,n)] # could not get to work well..Typicall use numpy or pandas or csv module and do not open and write etc to files with core python...unfamiliar with this, so using numpy 
    with open(fileName, "w") as file:
        for item in values:
            file.write(f'{item}'+' ')
    return values



def dataRead(fileName):
    with open(fileName, "r") as file:
        data = file.read().split()
        data = [int(elem) for elem in data] 
        return data



def sumFile(fileName1, fileName2, k):
    list1 = dataRead(fileName1)
    list2 = dataRead(fileName2)
    pairs_pos = []
    for i in list1:
        for j in list2:
            if (i+j) == k:
                pairs_pos.append((i,j)) # could increment i and j within their loops to only search for first one. Instructions do not say to do this. Results seem to show this though. On discussion post, recall seeing that the sample output was to be updated once this was pointed out...
    return pairs_pos


# # testing above code:  
# dataGen(5,1,4,"randoFile1.txt")
# dataGen(5,1,4,"randoFile2.txt")
# print("randoFile1 contents: \n",dataRead("randoFile1.txt"),"\n")
# print("randoFile2 contents: \n",dataRead("randoFile2.txt"),"\n")
# print(sumFile('randoFile1.txt','randoFile2.txt',4))

      
