'''Given some numbers in a line, return how many numbers are in that line . the numbers may separate by space'''
def count(n):
    while n > 0:
        line = input()
        lis = line.split()
        count = len(lis)
        print(count)
        n -= 1
        
count(int(input()))
#Python’s re module lets you split by any pattern, not just one character{lis.re.split()}. (Split wherever there’s a comma or a space — or even several of them.)
