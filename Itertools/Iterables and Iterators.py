#Answer to Iterables and Iterators

from itertools import combinations
n = input()
t = list(combinations(input().split(),int(input())))
print(len([i for i in t if 'a' in i])/len(t))