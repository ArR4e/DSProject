from pykkar import *

create_world("""
###########
#         #
#   <     #
#         #
#         #
###########
""")

while not is_wall():
    step()
    if is_wall():
        right()
        while not is_wall():
            step()
            if is_wall():
                right()
                paint()
        