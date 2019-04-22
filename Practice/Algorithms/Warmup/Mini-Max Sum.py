# Answer to Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
