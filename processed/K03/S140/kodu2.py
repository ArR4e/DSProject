from pykkar import *

create_world("""
#########
#       #
#       #
#       #
#       #
#   >   #
#########
""")

nurk = 4
while True:
    if is_wall():
        right()
        break
    else:
        step()
        
while nurk > 0:
    if is_wall():
        paint()
        nurk -= 1
        right()
    else:
        step()
