from pykkar import *
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")
while not is_wall():
    step()
nurgad = 4
while nurgad != 0:
    while not is_wall():
        step()
    paint()
    right()
    nurgad -= 1

paint()