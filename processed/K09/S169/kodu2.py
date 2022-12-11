from random import randint
def minu_shuffle(list):
    for a in range(len(list)*5):
        index = randint(0,len(list)-1)
        a = list.pop(index)
        list.append(a)
a= [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(a)
print(a)