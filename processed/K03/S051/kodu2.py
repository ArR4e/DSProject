from pykkar import *

create_world("""
########
#      #
#      #
#   v  #
#      #
#      #
########
""")

# jalutab nurgani
while not is_wall():
    step()
right()
while not is_wall():
    step()

# värvib nurgad
i = 0
while i < 4:
    i += 1
    paint()
    right()
    if i < 4:
        while not is_wall():
            step()

exitonclick()