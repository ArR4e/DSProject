from pykkar import *

create_world("""
#########
#       #
#       #
#       #
#       #
#  >    #
#########
""")
counter = 0
while not is_wall():
    step()
while is_wall():
    right()
    while not is_wall():
        if counter == 4:
            break
        else:
            step()
            while is_wall():
                paint()
                right()
                counter += 1



