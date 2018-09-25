#Answer to Find a string

def count_substring(string, sub_string):
    l=0
    i=0
    while i < len(string):
        if(string[i]==sub_string[0]):
            k=0
            for j in range(0,len(sub_string)):
                if(i+j<len(string) and string[i+j]!=sub_string[j]):
                    k=1
                elif(i+j>=len(string)):
                    k=1
            if(k==0 and j==len(sub_string)-1):
                l+=1
        i+=1
    return l