#Answer to Day 12: Inheritance

class Student(Person):
    def __init__(self,firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores=scores
    def calculate(self):
        l,total=len(self.scores)-1,0
        while(l>=0):
            total+=self.scores[l]
            l-=1
        total//=len(self.scores)
        if(total>=90):
            return 'O'
        elif(total>=80):
            return 'E'
        elif(total>=70):
            return 'A'
        elif(total>=55):
            return 'P'
        elif(total>=40):
            return 'D'
        else:
            return 'T'
#The below code is a solution to the bug in the question. The below code removes the extra space we encounter when we return the Grade from the above Class. To check the difference, delete the entire code below this line and you will see two spaces after "Grade:" while if you add the below lines of code, you can avoid that.
print_object = print
def print(*items_to_print):
    if 'Grade: ' in items_to_print:
        items_to_print = map(str, items_to_print)
        
        print_object(''.join(items_to_print))
    else:
        print_object(*items_to_print)