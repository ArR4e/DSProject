from pykkar import *

create_world("""
########
#      #
#   >  #
#      #
#      #
#      #
########
""")

cornerCount = 0
initialMovement = True

while not cornerCount == 4:
    while not is_wall() and initialMovement:
        step()
    if initialMovement:
        right()
        initialMovement = False
    while not is_wall():
        step()
    paint()
    cornerCount += 1
    right()