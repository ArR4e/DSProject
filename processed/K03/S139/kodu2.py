from pykkar import *

create_world("""
##########
#        #
#        #
#        #
#        #
#        #
#   >    #
##########
""")

while not is_wall():
    step()
right()
while not is_wall():
    step()
paint()
right()
i = 0
while i < 3:
    while not is_wall():
        step()
    right()
    paint()
    i += 1
        