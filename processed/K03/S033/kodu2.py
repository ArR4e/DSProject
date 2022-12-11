from pykkar import *

create_world("""
########
#      #
#      #
#   <  #
#      #
#      #
########
""")

while not is_wall():
    step()
right()
n = 4
while n > 0:
    while not is_wall():
        step()
    paint()
    right()
    n -= 1
    print(n)