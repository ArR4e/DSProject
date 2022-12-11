from pykkar import *

create_world("""
###############
#             #
#             #
#      <      #
#             #
###############
""")

poore = 0

while not is_wall():
    step()
    if is_wall():
        right()
        poore += 1
        if is_wall():
            right()
        if poore > 1:
            paint()


exitonclick()