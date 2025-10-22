'''Given an integer find out if the integer is even or odd. (long integer) 
   Remember in Python we don't have any problem with the integer size as the int object takes care of that
   If you use C or CPP you will need (long long int) as your type of the variable. '''

def even_or_odd(count):
    while(count!=0):
        num = int(input())# Input() function returns a string so we need to type cast it to integer 
        count -= 1
        if num % 2 ==0:
            print('even')
        else:
            print('odd')
            

even_or_odd(int(input()))        