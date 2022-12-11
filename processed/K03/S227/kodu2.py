from pykkar import *
create_world("""
#############
#           #
#           #
#     >     #
#           #
#           #
#           #
#############""")
while not is_wall():
    step()
right()
x=4
while x != 0:
    while not is_wall():
        step()
    paint()
    right()
    x-=1