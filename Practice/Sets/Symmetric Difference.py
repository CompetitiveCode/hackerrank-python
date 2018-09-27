#Answer to Symmetric Difference

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
c = a&b #This gives the common element in both the sets
d = set()
d = sorted(d.union(a - c).union(b - c)) #Taking the union of both the sets with the difference from set c and sorting it
for i in d:
    print(i)
    
"""
If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']

If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]

Sets are an unordered bag of unique values. A single set contains values of any immutable data type.
"""