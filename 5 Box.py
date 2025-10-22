''' you will be given value of a side of a rectangle . you will draw a rectangle box with it'''

def box(side_length):
    for i in range(side_length):
        for j in range(side_length):
            print('*',end=' ') # the end = will prevent printing a new line or your output will be a long line not a square 
        print()# this will take us to the next line or all our * will be printed in the same line

box(int(input()))