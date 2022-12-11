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
    step()
    step()
    paint()
    right()
    step()
    step()
    step()
    step()
    paint()
    right()
    step()
    step()
exitonclick()