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

while is_wall() == False:
    step()
    if is_wall() == True:
        right()
        while is_wall() == False:
            step()
            if is_wall() == True:
                paint()
                right()