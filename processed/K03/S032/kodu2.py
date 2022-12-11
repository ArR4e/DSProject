from pykkar import *

create_world("""
#################
#               #
#               #
#               #
#               #
#               #
#v              #
#################
""")


while not is_wall():
    step()
right()

i=1
while i<=4:
    while not is_wall():
        step()
    right()
    paint()
    i+=1
