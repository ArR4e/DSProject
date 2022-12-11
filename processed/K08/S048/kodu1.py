from random import sample
def bingo():
    a= sample(range(1,11), 3)
    b= sample(range(11,21),2)
    järjend= a+ b
    return järjend

print(bingo())