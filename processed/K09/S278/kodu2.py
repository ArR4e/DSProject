# Pythoni moodulis random on funktsioon shuffle, mis ajab argumendiks antud järjendis elementide järjekorra juhuslikult segamini:
# >>> from random import shuffle
# >>> a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
# >>> shuffle(a)
# >>> a
# [5, 3, 6, 5, 5, 3, 4, 1, 6]
# Kirjuta ise analoogne funktsioon minu_shuffle, seejuures pole lubatud kasutada olemasolevat shuffle-funktsiooni.
# Automaatkontroll. Tuleks jälgida, et funktsioon tõstaks elemendid ümber talle etteantud listis, mitte ei tagastaks uut listi.
import random

def minu_shuffle(random_list):
    for i in range(len(random_list)-1, 0, -1):
        random_index = random.randint(0, i + 1)
        random_list[i], random_list[random_index] = random_list[random_index], random_list[i]
        return(random_list)