'''write a program to get the factorial of the given number'''
def factorial(n):
    while n>0:
        num = int(input())
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print(factorial)
        n-=1
        
factorial(int(input()))