from pykkar import *
from math import inf
create_world("""
########
#      #
#   >  #
#      #
#      #
#      #
########
""")
i = 0

while not is_wall():
    step()

right()
while not is_wall():
    step()

right()
while True:
    step()
    if is_wall():
        paint()
        right()
        i += 1
        if i > 3:
            break