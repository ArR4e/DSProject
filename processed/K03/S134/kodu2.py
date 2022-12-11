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
a = 1
while not is_wall():
    step()
while is_wall():
    paint()
    right()
while not is_wall():
    step()
while is_wall():
    paint()
    right()
    while not is_wall():
        step()
while is_wall():
    paint()
    right()
while not is_wall():
    step()
while is_wall():
    paint()
    right()