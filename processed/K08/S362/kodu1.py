from random import sample
def bingo():
    järjend1=sample(range(1,11),3)
    while järjend1==[1, 2, 3]or järjend1==[3, 2, 1]or järjend1==[2, 1, 3] or järjend1==[2, 3, 1]or järjend1==[3, 1, 2]or järjend1==[1, 3, 2]:
        järjend1=sample(range(1,11),3)
    järjend2=sample(range(11,21),2)
    suur_järjend=järjend1+järjend2
    return suur_järjend




järjend1=sample(range(1,11),3)
järjend2=sample(range(11,21),2)

# print(järjend1)
# print(järjend2)

print(bingo())