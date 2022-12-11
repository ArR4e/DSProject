from random import sample

def bingo():
    while True:
        järjend = []
        järjend += sample(range(1,11), 3)
        järjend += sample(range(11,20), 2)
        print(järjend)
        
bingo()
