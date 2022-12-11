import random
def minu_shuffle(inputlist):
    for index,value in enumerate(inputlist):
        n = random.randint(0,len(inputlist)-1)
        inputlist[index] = inputlist[n]
        inputlist[n] = value
