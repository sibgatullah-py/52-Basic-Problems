'''Write a program that will find out the divisors of the given number'''

def divisor(n):
    for i in range(1,n+1):
        num = int(input())
        lis = []
        for j in range(1,num+1):
            if num % j == 0:
                lis.append(j)
        print(f'Case {i}:',*lis) # the * unpacks the list

divisor(int(input()))
        