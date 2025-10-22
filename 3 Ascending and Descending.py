'''Write a program that counts from 100 to 1 and 1 to 100 as Ascending and Descending'''

def ascending():
    i = 1
    while i <= 100:
        print(i)
        i+=1
def descending():
    i = 100
    while i >= 1:
        print(i)
        i-=1
        
ascending()
descending()