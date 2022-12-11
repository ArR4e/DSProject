from pykkar import *

create_world("""
#######
#     #
#  v  #
#     #
#     #
#     #
#######
""")

while not is_wall():
    step()
right()

x = 0
while x < 4:
    while not is_wall():
        step()
    paint()
    right()
    x += 1