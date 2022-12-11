import random
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(a):
    b=[]
    c=a+[]
    for i in c:
        random_num = random.choice(a)
        b.append(random_num)
        #a.remove(random_num)
    a=b
    #return a
      
minu_shuffle(a)