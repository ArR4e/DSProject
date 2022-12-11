from random import sample

def bingo():
    while True:
        arvud = []
        arvud.append(sample(range(1, 11), 3))
        arvud.append(sample(range(11, 21), 2))  
        arvud = [item for sublist in arvud for item in sublist]
#https://stackoverflow.com/questions/25674169/how-does-the-list-comprehension-to-flatten-a-python-list-work
        if 1 in arvud and 2 in arvud and 3 in arvud:
            pass
        else:
            break
    
    return arvud
print(bingo())