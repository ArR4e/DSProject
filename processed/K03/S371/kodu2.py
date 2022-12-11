from pykkar import *

create_world("""
##########
#        #
#        #
#        #
#        #
#   <    #
##########
""")

while not is_wall():
    step()
right()
for i in range(4):
    while not is_wall():
        step()
    paint()
    while is_wall():
        right()

