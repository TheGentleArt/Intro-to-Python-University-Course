# Justin Williams
# Assignment 03
# EPD 455: Python for Applications in Engineering
# 2022-10-06
#
# =============================================================================
# Problem 05
# Write a python class Point with the following methods and attributes.
# (a) The point class should have two attributes, the x and y coordinates. The default values
# for these two attributes should be (0,0)
# (b) Write a __str__ or __repr__ method to print (x,y) when print is called on an instance of
# (c) Write methods getX() and getY() that return the X and Y coordinates of the point
# respectively.
# (d) Write a method reflectX() that returns a point instance that is a mirror image of the
# point about the X axis.
# (e) Similarly, write method reflectY().
# (f) Write a method slope(point) that takes a point as input and returns the slope of the line
# joining the two points.
# 2(g) Finally, write a method getEq(point) that takes a point as input, calculates the slope m
# using the slope and the constant c method and returns a function which evalautes to
# mx + c for any given x.
# =============================================================================
#

class point:
    """This is a class for a point somewhere in 2D space. For 3D space make your own friggin point class"""
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        
    def __str__(self): # could also use __repl__? do no yet understand differences...need to go back and review
        return (f'({self.x}, {self.y})')
    
    def getX(self): # requires () after self.getX
        return self.x
    
    def getY(self):
        return self.y
    
    def reflectX(self):
        return point(self.x, -self.y)
    
    def reflectY(self):
        return point(-self.x, self.y)
    
    def slope(self, point):
        # m = rise/run = (y2-y1)/(x2-x1)
        m = (point.y-self.y)/(point.x-self.x)
        return m

    def getEq(self, point): # not sure about how to return this function, how is this planned to be used exactly?
        m = self.slope(point)
        b = self.y - m*self.x
        def returnfunc(x):
            y = m*x + b
            return y
        return returnfunc()
        
    
