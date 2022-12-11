from random import sample

def minu_shuffle(list):
    list_copy = list[:]
    numbrite_list = sample(range(0, len(list)), len(list))
    for i in range(len(list)):
        list[i] = list_copy[numbrite_list[i]]
    



    