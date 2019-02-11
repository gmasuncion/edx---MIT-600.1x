from decimal import Decimal
import math
def remaining(balance, annualInterestRate, monthlyPaymentRate):
    '''
    num, num, num -> num
    
    Returns the balance remaining to be paid after one year.
    '''
    
    months = 0
    remaining = 0

    while months < 12:
        rate = annualInterestRate / 12.0
        min_payment = balance * monthlyPaymentRate
        unpaid_balance = balance - min_payment
        interest = unpaid_balance * rate
        remaining = unpaid_balance + interest
        balance = remaining
        months += 1
        print(balance)
        
    remaining = round(remaining, 2)
    print("Remaining Balance:", remaining)
    return remaining
        

def min_payment(balance, annualInterestRate):
    '''
    num, num -> num
    
    Returns the amount to be paid monthly to rid the debt owed in a year.
    '''
    reset = balance
    remaining = 0
    per_month = 0
    rate = annualInterestRate / 12.0

    while balance > 0:
        for i in range(12):
            min_payment = per_month
            unpaid_balance = balance - per_month
            interest = unpaid_balance * rate
            remaining = unpaid_balance + interest
            balance = remaining
        if balance > 0:
            balance = reset
            per_month += 10
            
    print('Lowest Payment:', per_month)
    

def precise_min_payment(balance, annualInterestRate):
    '''
    num, num -> num
    
    Returns the precise amount to be paid monthly to rid the debt owed.
    Utilizes Bisection search method.
    '''
    
    reset = balance
    rate = annualInterestRate / 12.0
    upper_bound = balance * (1 + rate)**12 / 12.0
    lower_bound = balance / 12
    remaning = 0
    per_month = 0
    epsilon = 0.01
    per_month = 0

    while abs(balance) > epsilon:
        mid = (upper_bound + lower_bound) / 2
        for i in range(12):
            per_month = mid
            unpaid_balance = balance - per_month
            interest = unpaid_balance * rate
            remaining = unpaid_balance + interest
            balance = remaining
        if abs(balance) < epsilon:
            print(round(per_month,2))
        else:
            if balance < epsilon:
                upper_bound = mid
                balance = reset
            elif balance > epsilon:
                lower_bound = mid
                balance = reset

    