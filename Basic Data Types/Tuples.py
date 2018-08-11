#Answer to Tuples

if __name__ == '__main__':
    t=()
    n = int(input())
    integer_list = map(int, input().split())
    for i in integer_list:
        t = t+(i,)
    print(hash(t))