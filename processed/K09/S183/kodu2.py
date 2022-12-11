import random
def minu_shuffle(järjend):
    n = len(järjend)
    for i in range(n):
        juhuslik = random.randint(0, n-1)
        järjend[i], järjend[juhuslik] = järjend[juhuslik], järjend[i]