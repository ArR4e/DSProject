from pykkar import *

create_world("""
############
#          #
#          #
#          #
# >        #
#          #             
#          #
############
""")

while not is_wall():
    step()
    if is_wall():
        right()
        paint()
    if is_wall():
        right()
        right()