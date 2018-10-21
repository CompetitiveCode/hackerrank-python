#Answer to Floor, Ceil and Rint

import numpy
a=list(map(float,input().split()))
a=numpy.array(a)
numpy.set_printoptions(sign=' ') #This is only required to add a whitespace in the output, else would not be required.
print(numpy.floor(a),numpy.ceil(a),numpy.rint(a),sep="\n")

"""
floor 

The tool floor returns the floor of the input element-wise. 
The floor of x is the largest integer i where i<=x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

ceil 

The tool ceil returns the ceiling of the input element-wise. 
The ceiling of x is the largest integer i where i>=x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

rint 

The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""