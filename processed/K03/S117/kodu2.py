# alustasin 13.09.2021 (22:03)
from pykkar import *

create_world("""
#########
#       #
#    ^  #
#       #
#       #
#########
""")
while not is_wall():
    step()
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
right()
while not is_wall():
    step()
paint()