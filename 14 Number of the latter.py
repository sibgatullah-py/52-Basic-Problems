# given a sentence , find out how many times is the given latter present in the sentence 

def latter_count(n):
    while n > 0:
      sentence = input()
      latter = input()
      count = 0
      for i in sentence:
          if i == latter:
              count += 1
      print(count)
      n-=1
      
latter_count(int(input()))