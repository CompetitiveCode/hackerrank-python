#Answer to Day 19: Interfaces

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        temp = 0
        for i in range(1,n+1):
            if(n%i == 0):
                temp+=i
        return temp