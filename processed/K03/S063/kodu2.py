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

while not is_wall():
    step()
    if is_wall():
        if not(is_painted()):
            paint()
            right()
            continue
        else:
            right()
            break

exitonclick()