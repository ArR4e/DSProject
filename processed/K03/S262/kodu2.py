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

nurki_jaanud = 5
if get_direction() == "N":
    right()
elif get_direction() == "S":
    right()
    right()
    right()
elif get_direction() == "W":
    right()
    right()

while nurki_jaanud > 0:
    if is_wall():
        if nurki_jaanud == 5:
            nurki_jaanud -= 1
            right()
        else:
            nurki_jaanud -= 1
            paint()
            right()
            if nurki_jaanud > 0:
                step()
    else:
        step()