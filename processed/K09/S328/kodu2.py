from random import choice
def minu_shuffle(a):
    result = []
    for i in range(len(a)):
        random_int = choice(a)
        index = a.index(random_int)
        result.append(random_int)
        a.remove(a[index])
    print(result)
