from pykkar import *

create_world("""
##########
#        #
#        #
#     v  #
#        #
##########
""")

i = 1
for i in range(4):
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    paint()
    i += 1