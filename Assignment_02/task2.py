# Justin Williams
# Assignment 02
# EPD 455: Python for Applications in Engineering
# 2022-09-25
#
# Question 2
# Assignment Instruction:
# Assume that: f is a continuous function; f (a) · f (b) < 0 for some known values a and b; and a < b. Then, there exists some value c ∈ (a, b) such that f (c) = 0. In other words, the function f has a root in the interval (a, b).
# Write a function root(f,a,b),that takes a function f and two float variables a and b and returns a value that is a close approximation, say within 10−6, of the root c ∈ (a, b) of f .
# Note: This function does not take command line arguments but will rather be imported into another python script and called from there.
# int: Check the sign at the mid point of the interval and recurse.
# Submit the python script as task2.py on Canvas.
#
    
def f(x):
    return (x**2)-7

def root(f,a,b,tol):
    lim_lower = min(a,b)
    lim_upper = max(a,b)
    while ( (lim_upper-lim_lower) >= tol ):
        midpoint = (lim_upper + lim_lower)/2  # midway (avg) between two limits
        res_lower = f(lim_lower)  # y-value of lower limit plugged into function
        res_upper = f(lim_upper)  # y-value of upper limit plugged into function
        res_mid = f(midpoint)  # y-value of midpoint between limits plugged into function
        if (res_lower * res_mid) < 0:  # if midpoint y-value and lower limit y-value prodcut is negative, means one is negative and the other is positive
            lim_upper = midpoint  # change new upper limit to midpoint value
        elif (res_upper * res_mid) < 0:  # if midpoint y-value and upper limit y-value product is negative, means one is negative and other is positive
            lim_lower = midpoint  # change new lower limit to midpoint value
            print(lim_lower,"   ;   ",lim_upper)
        else:
            return    print("maybe there is more than one root? Check limits before trying again...")
    return midpoint # once lower and upper limits are within tolerance value of each other, return the average between these limits

# Test
root_x_loc = root(f,-0.1,5.3,1e-6)
print("A root was found at ~ x=", root_x_loc)
