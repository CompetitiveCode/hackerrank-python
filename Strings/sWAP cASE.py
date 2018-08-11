#Answer to sWAP cASE

def swap_case(s):
    j = ""
    for i in s:
        if(i.islower()):
            j=j+i.upper()
        elif(i.isupper()):
            j=j+i.lower()
        else:
            j=j+i
    return j