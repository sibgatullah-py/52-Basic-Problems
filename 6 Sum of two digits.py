'''Given a number oof 5 digits . return the sum of first and last digit of that number'''

def sum(n):
    while n > 0 :
        num = int(input())
        first_digit = num
        last_digit = num % 10 # % 10 always gives the last digit.
        while first_digit >= 10:
            first_digit //= 10 # // 10 repeatedly removes the last digit until only the first digit remains.
            
        print(' Sum = ',first_digit+last_digit)

sum(int(input()))