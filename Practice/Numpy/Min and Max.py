#Answer to Min and Max

import numpy
n,m=map(int, input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(numpy.max(numpy.min(numpy.array(a),axis=1)))

"""
min

The tool min returns the minimum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

max

The tool max returns the maximum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7

By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.
"""