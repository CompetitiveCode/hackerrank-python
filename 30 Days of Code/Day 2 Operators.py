#Answer to Day 2: Operators

def solve(meal_cost, tip_percent, tax_percent):
    meal_cost+=((meal_cost/100)*tip_percent)+((meal_cost/100)*tax_percent)
    print("The total meal cost is "+str(round(meal_cost))+" dollars.")

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)