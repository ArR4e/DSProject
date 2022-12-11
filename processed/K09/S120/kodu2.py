from random import choice

def minu_shuffle(lst):
    temp_list = lst[:]
    index_choices = [i for i in range(len(lst))]
    for i in temp_list:
        random_index = choice(index_choices)
        lst[random_index] = i
        index_choices.remove(random_index)
