from random import sample
järjend = []
x = sample(range(1, 11), 3)
y = sample(range(11, 21), 2)
def bingo(x, y):
    järjend = x + y
    return järjend
print("bingo()")
print(bingo(x, y))
