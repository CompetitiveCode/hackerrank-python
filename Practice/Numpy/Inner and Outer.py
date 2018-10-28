#Answer to Inner and Outer

import numpy
a=numpy.array(list(map(int,input().split())))
b=numpy.array(list(map(int,input().split())))
print(numpy.inner(a,b),numpy.outer(a,b),sep="\n")

"""
inner

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4

outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
"""