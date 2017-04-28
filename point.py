# point.py
#
# ICS 32 Spring 2014
# Code Example
#
# This module contains a Point class.  Objects of this class
# represent points in a two-dimensional space that can report
# their coordinates in both fractional and absolute coordinate
# systems.  They are created using either a fractional or an
# absolute coordinate system, then can be asked to translate
# themselves to either system.
#
# The idea is that a point in the fractional system corresponds
# naturally to a point in the absolute system, and vice versa.
# So rather than spread the code that performs these conversions
# throughout our program, we're better off creating a tool to make
# this kind of conversion simpler.  We could manipulate text without
# string objects, but string objects make the job easier by providing
# a variety of useful methods like strip(), split(), and upper().
# Similarly, our Point objects provide the raw materials to
# handle coordinate system conversions for points in two-dimensional
# space.

import math



class Point:
    def __init__(self, frac: (float, float), absolute: (int, int), absolute_size: (int, int)):
        '''
        Initializes a Point object.  The expectation is that either
        the frac parameter *or* the absolute and absolute_size parameters
        are specified, but not both.  Those that are not specified will have
        the value None.
        '''
        if frac == None:
            abs_x, abs_y = absolute
            abs_size_x, abs_size_y = absolute_size

            self.frac_x = abs_x / abs_size_x
            self.frac_y = abs_y / abs_size_y
        else:
            frac_x, frac_y = frac
            self.frac_x = frac_x
            self.frac_y = frac_y


    def frac(self) -> (float, float):
        '''
        Returns an (x, y) tuple that contains fractional coordinates
        for this Point object.
        '''
        return (self.frac_x, self.frac_y)


    def absolute(self, absolute_size: (int, int)) -> (int, int):
        '''
        Returns an (x, y) tuple that contains absolute coordinates for
        this Point object.  The width and height are used to make
        the appropriate conversion -- absolute coordinates change as width
        and height changes.
        '''
        abs_size_x, abs_size_y = absolute_size
        return (int(self.frac_x * abs_size_x), int(self.frac_y * abs_size_y))


    def frac_distance_from(self, p: 'Point') -> float:
        '''
        Given another Point object, returns the distance, in
        terms of fractional coordinates, between this Point and the
        other Point.
        '''

        # Per the Pythagorean theorem from mathematics, the distance
        # between two points is the square root of the sum of the
        # squares of the differences in the x- and y-coordinates.
        return math.sqrt(
            (self.frac_x - p.frac_x) * (self.frac_x - p.frac_x)
            + (self.frac_y - p.frac_y) * (self.frac_y - p.frac_y))

        # Note, too, that there's a function in the Python standard
        # library, math.hypot, that does exactly this calculation.



# These two functions are used to create Points that are either
# being created from fractional or absolute coordinates.  Given these
# two functions, we'll never create Point objects by calling the
# Point constructor; instead, we'll just call the appropriate
# of these two functions, depending on whether we have fractional or
# absolute coordinates already.

def from_frac(frac: (float, float)) -> Point:
    '''Builds a Point given fractional x and y coordinates.'''
    return Point(frac, None, None)



def from_absolute(absolute: (int, int), absolute_size: (int, int)) -> Point:
    '''
    Builds a Point given absolute x and y coordinates, along with
    the width and height of the absolute coordinate area (necessary for
    conversion to fractional).
    '''
    return Point(None, absolute, absolute_size)

    
