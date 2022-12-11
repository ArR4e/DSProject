from pykkar import *


create_world("""
#########
#       #
#       #
#       #
#       #
#    >  #
#########
""")

while not is_wall():
    step()
paint()
right()
if is_wall():
    right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()

