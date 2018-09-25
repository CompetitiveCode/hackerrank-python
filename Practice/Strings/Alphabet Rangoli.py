#Answer to Alphabet Rangoli

def print_rangoli(size):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i=size
    k=0
    while i>0:
        print("-"*((2*size)-2-(k*2)),end="")
        j=size-1
        while j>=i:
            print(alpha[j],end="-")
            j-=1
        while j<size:
            print(alpha[j],end="")
            j+=1
            if(j!=size):
                print("-",end="")
        print("-"*((2*size)-2-(k*2)),end="\n")
        i-=1
        k+=1
    k-=1
    i=size-1
    p=1
    while i>0:
        print("-"*((2*size)-(k*2)),end="")
        j=size-1
        while j>=p:
            print(alpha[j],end="-")
            j-=1
        j+=2
        while j<=size-1:
            print(alpha[j],end="-")
            j+=1
        print("-"*((2*size)-1-(k*2)),end="\n")
        i-=1
        k-=1
        p+=1