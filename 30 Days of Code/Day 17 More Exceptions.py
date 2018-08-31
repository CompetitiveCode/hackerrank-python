#Answer to Day 17: More Exceptions

class Calculator:
    @staticmethod
    def power(n, p):
        if (n < 0 or p < 0):
            raise ValueError('n and p should be non-negative')
        return n ** p