from random import sample
def bingo():
    while True:
        esimesed = sample(range(1, 11), 3)
        teised = sample(range(11, 21), 2)
        järjend = esimesed + teised
        if "1" in järjend and "2" in järjend and "3" in järjend:
            continue
        else:
            return(järjend)
            break
        
            
