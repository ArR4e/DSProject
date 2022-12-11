from random import sample
def bingo():
    while True:
        list1 = sample(range(1,11),3)
        if [1,2,3] != sorted(list1):
            list2 = sample(range(11,21),2)
            return list1 + list2
print(bingo())