#Answer to The Captain's Room

k,arr = int(input()),list(map(int, input().split())) #Getting the input
myset = set(arr) #Getting the unique elements in the list
print(((sum(myset) * k) - (sum(arr))) // (k - 1))
#Multiply the sum of unique numbers by k (as if every room number was repeated k times).
#Subtract the sum of given room numbers. The difference will be (k-1)*captains_room_number. Divide by (k-1) to get the captains room number