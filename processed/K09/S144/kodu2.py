from random import randint
def minu_shuffle(järjend):
    järjekord = []
    for i in range(len(järjend)):
        while True:
            n = randint(0, len(järjend)-1)
            if n in järjekord:
                continue
            else:
                järjekord.append(n)
                break
    järjend[:] = [järjend[i] for i in järjekord]
