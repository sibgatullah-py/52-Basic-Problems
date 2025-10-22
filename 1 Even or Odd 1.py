'''Given an integer find out if the integer is even or odd'''

def even_or_odd(count):
    while(count!=0):
        num = int(input())# Input() function returns a string so we need to type cast it to integer 
        count -= 1
        if num % 2 ==0:
            print('even')
        else:
            print('odd')
            

even_or_odd(int(input()))        