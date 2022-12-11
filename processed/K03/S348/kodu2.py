from pykkar import *

create_world("""
########
#      #
#      #
#  v   #
#      #
#      #
########
""")

i = 1
while i < 5:
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    paint()
    i += 1
    