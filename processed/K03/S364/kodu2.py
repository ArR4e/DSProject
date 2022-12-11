from pykkar import *

create_world("""
########
#   >  #
#      #
#      #
#      #
#      #
########
""")
while not is_wall():
    step()
right()
for iljusha in range(4):
    while not is_wall():
        step()
    paint()
    right()


