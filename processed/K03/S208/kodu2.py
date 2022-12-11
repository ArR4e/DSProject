from pykkar import *
create_world("""
######
#    #
#  > #
#    #
#    #
######
""")
while not is_wall():
        step()
right()
samme = 4
while samme > 0:
    while not is_wall():
        step()
    right()
    paint()
    samme -= 1
paint()
