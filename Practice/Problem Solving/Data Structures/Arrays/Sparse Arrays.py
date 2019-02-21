#Answer to Sparse Arrays - https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchingStrings(strings, queries):
    result = []
    for i in queries:
        count = 0
        for j in strings:
            if j == i:
                count+=1
        result.append(count)
    return result

strings_count = int(input())
strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())
queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)

for i in res:
    print(i)