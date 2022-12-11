from pykkar import *

create_world("""
########################
#                      #
#                      #
#                      #
#                      #
#    <                 #
########################
""")

# Sõltumata algsest asukohast viin programmi abil pykkari alati ühte punkti

suund = get_direction()

if suund == N:
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    right()
    
elif suund == E:
    while not is_wall():
        step()
    right()
    right()
    right()
    while not is_wall():
        step()
    right()
    right()

elif suund == S:
    right()
    right()
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    right()

elif suund == W:
    right()
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    right()

#

paint()

i = 1

while i < 4:
    while not is_wall():
        step()
    paint()
    right()
    i += 1

exitonclick()