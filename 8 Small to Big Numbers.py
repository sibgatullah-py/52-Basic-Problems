def ascending(n):
    while n > 0:
        lis = []
        for i in range(3):
            lis.append(int(input()))
        lis.sort()
        print(*lis)
        n -= 1
        
ascending(int(input()))