from pykkar import *

create_world("""
#######
# >   #
#     #
#     #
#     #
#     #
#     #
#######
""")

def detect_wall():
    while True:
        step()
        if is_wall() == True:
            break

detect_wall()
right()
detect_wall()
paint()
right()
detect_wall()
paint()
right()
detect_wall()
paint()
right()
detect_wall()
paint()
paint()