# count how many times every single latter is present in the sentence 
def count(n):
    while n > 0:
        S = input()
        count=[0]*26 # Creating an empty list with 0,1,2 indexes representing the latter ascii values 
        for i in S:
            if 'a' <= i <= 'z':
                # The ord function helps us to get the ascii value of the character . 
                i = ord(i) - ord('a') # Finding which index matches with the latter we got from looping over the string a = 97 . 97-97 = 0 so it means we got a value for 0 indexed item
                count[i]+=1 # when we make sure which index box we got and making it's value 1 plus from 0
        for i in range(26):
            if count[i]>0:
                print(f"{chr(i+ord('a'))} : {count[i]}")# adding the ascii value of str a with the index so we can print the character with chr() function and the print how many value we got in each box
        n-=1
        
count(int(input()))