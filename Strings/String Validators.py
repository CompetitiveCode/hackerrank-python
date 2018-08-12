#Answer to String Validators

if __name__ == '__main__':
    s = input()
    a = b = c = d = e = False
    for i in s:
        if(i.isalnum()):
            a=True
        if(i.isalpha()):
            b=True
        if(i.isdigit()):
            c=True
        if(i.islower()):
            d=True
        if(i.isupper()):
            e=True
    print(a,b,c,d,e,sep="\n")