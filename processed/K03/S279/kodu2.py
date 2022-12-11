from pykkar import *

create_world("""
########
#      #
#      #
#      #
#     >#
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
    if False:
        continue
right()

nurgad = 4
while nurgad > 0:
    while not is_wall():
        step()
        if False:
            continue
    paint()
    right()
    nurgad -= 1
