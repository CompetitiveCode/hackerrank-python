#Answer to List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print("[", end="")
    for i in range( x + 1):
        for j in range( y + 1):
            for k in range (z + 1):
                if ( ( i + j + k) != n ):
                    print("["+str(i)+", "+str(j)+", "+str(k)+"]", end="")
                    if (((x) != i) or ((y) != j) or ((z) != k)):
                        print(", ", end="")
    print("]")