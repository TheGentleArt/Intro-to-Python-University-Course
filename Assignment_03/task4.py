# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-06
#
# =============================================================================
# Problem 04
# Write a function printSentences(sentenceNums), that takes as input a list of integers sentenceNums
# representing sentence numbers, and prints out the sentence corresponding to the sentence num-
# ber from The Time Machine by H.G.Wells. Print each sentece on seperate lines. Using if-else
# conditions is not allowed within the function.
# Note - For this problem, consider a sentence as a line .i.e. a sentence starts and ends with \n
# (new line character) rather than a full stop.
# Submit the python script task4.py on Canvas.
# =============================================================================
#


def printSentences(sentenceNums):
    with open('time_machine_500.txt', 'r') as file:
        lines = file.readlines()
        for line in sentenceNums:
            print(lines[line])

# # test case
# a = printSentences([-1,-2, -4, -3])
