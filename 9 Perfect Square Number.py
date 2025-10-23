'''Given a number . determine if the number is a perfect square number or not'''
import math

def square(n):
    while n > 0:
        num = int(input())
        root = math.sqrt(num)
        if root * root == num:
            print('YES')
        else:
            print('NO')
        n -= 1
            
square(int(input()))