# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-07
#
# =============================================================================
# Problem 06
# Generate a matrix A of size 500 × 500 containing random floats between -1.0 and 1.0 using numpy.
# Compute A + A, AAT ,AT A and the frobenius norm of A. Print each of these in seperaete lines,
# one after the other in the same order.
# =============================================================================
#
# whattheheckisthisfrobeniusnormstuff

import numpy as np
from numpy import linalg as LA

A = np.random.uniform(-1.0,1.0,[500,500])
print("A is: ", A)
print("________________________\n\n\n\n\n")

AaddedA = A + A
print(AaddedA,'\n\n')

AtimesATranspose = A*A.transpose()
print(AtimesATranspose,'\n\n')

ATransposetimesA = A.transpose()*A
print(ATransposetimesA,'\n\n')

print(LA.norm(A, 'fro',),'\n\n')

