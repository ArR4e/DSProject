from pykkar import *

def left():
    for i in range(0,3):
        right()

create_world("""
#########
#       #
#       #
#       #
#  >    #
#       #
#########
""")

while is_wall() == False:
    step()
for i in range(0,4):
    left()
    while is_wall() == False:
        step()
    paint()