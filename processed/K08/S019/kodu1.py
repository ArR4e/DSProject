from random import sample

def bingo():
   b, c, d = sample(range(1,11),3)
   while b + c + d == 6:
       b, c, d = sample(range(1,11),3)
   e, f = sample(range(11,21),2)
   a =[b,c,d,e,f]
   
   return a