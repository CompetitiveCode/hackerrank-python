#Answer to Any or All

n=int(input())
a=list(map(int,input().split()))
print(all([j > 0 for j in  a])and any([str(j) == str(j)[-1:] for j in a]))

"""
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
"""