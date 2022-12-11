from pykkar import *

create_world("""
#########
#       #
#       #
#   ^   #
#       #
#       #
#########
""")

while not is_wall():
    step()
right()

while not is_wall():
    step()
paint()

i = 0

while i <= 2:
    right()
    while not is_wall():
        step()
    paint()
    i += 1
paint()