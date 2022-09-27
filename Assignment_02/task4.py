# Justin Williams
# Assignment 02
# EPD 455: Python for Applications in Engineering
# 2022-09-26
#
# Question 4
# Assignment Instruction:
# 4. Consider the sparse matrix,
#    (a) Complete the python script (task4.py) in the EPD 455 repository that adds all non-zero
#    elements in the nested list representing the sparse matrix above to the dictionary dict.
#    (b) In terms of storage space, is the nested lists better or the dictionary?
#    (c) Interestingly enough, these are only two of the methods commonly used to store sparse
#    matrices. Google three other methods used by the python library scipy and, in a sentence, explain one advantage and one disadvantage of each.
#    Submit the completed python script as task4.py on canvas.
#
# Directly below from: https://github.com/DanNegrut/EPD455-2022/blob/main/assignments/A02/task4.py
# =============================================================================
# #
# =============================================================================
# # creating sparse matrix
# arr = [[1, 0, 0, 18, 0],
#        [0, 36, 2, 0, 0],
#        [0, 0, 63, 0, 0],
#        [0, 0, 0, 10, 0],
#        [90, 0, 0, 0, 7]]
 
# # creating empty dictionary
# dic = {}
 
# # iterating through the matrix
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] != 0:
#             # Insert code here to add non zero elements to the 
#             # dictionary "dic"

# print("Position of non-zero elements in the matrix:")
# print(dic)
# =============================================================================
# #
# =============================================================================
#

# creating sparse matrix
arr = [[1, 0, 0, 18, 0],
        [0, 36, 2, 0, 0],
        [0, 0, 63, 0, 0],
        [0, 0, 0, 10, 0],
        [90, 0, 0, 0, 7]]
 
# creating empty dictionary
dic = {}
 
# iterating through the matrix
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != 0:
            dic[i,j] = arr[i][j]
            
print("Position of non-zero elements in the matrix:")
print(dic)

import sys # realize imports are typically at top, not sure of environment this will be used in, wanted other code to run first before erroring...
print("\nStorage space of nested list version: ",sys.getsizeof(arr))
print("Storage space of dictonary version: ",sys.getsizeof(dic))
if sys.getsizeof(arr) > sys.getsizeof(dic):
    print("Dictionary version is better for storage.")
elif sys.getsizeof(arr) == sys.getsizeof(dic):
    print("Same storage space either way.")
else:
    print("Nested list version is better for storage.")
