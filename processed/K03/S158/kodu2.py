from pykkar import *

create_world("""
#######
#     #
#     #
#     #
#   ^ #
#######
""")

#Et jõuaks nurka
while not is_wall():
    step()
right()
while not is_wall():
    step()
paint()
paint()
right()
while not is_wall():
    step()
paint()
paint()
right()
while not is_wall():
    step()
paint()
paint()
right()
while not is_wall():
    step()
paint()
paint()