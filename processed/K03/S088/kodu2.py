from pykkar import *

create_world("""
##############
#            #
#            #
#    >       #
#            #
#            #
#            #
#            #
##############
""")

## pykkar alustab alati näoga seinast eemal
if is_wall():
    right()
    right()
    
## liikumine seinani, pööre paremale, liikumine seinani
while not is_wall():
    step()
    if is_wall():
        right()
        while not is_wall():
            step()
            if is_wall():
                break
right()
paint()

## vaja värvida veel 3 nurka, loop kordub kuni i väärtus on väiksem kolmest
i = 0
while i < 3:
    while not is_wall():
        step()
        if is_wall():
            right()
            paint()
            i += 1
            break