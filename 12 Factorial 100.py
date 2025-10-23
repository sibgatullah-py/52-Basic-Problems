'''Find out how many 0 is there at the end of the factorial'''
def factorial(n):
    while n>0:
        num = int(input())
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        
        count = 0
        while count >= 0:
            mod = factorial % 10
            if mod == 0:
                count+=1
            else:
                break
            factorial //= 10
            
        print(count)
        n-=1
        
factorial(int(input()))