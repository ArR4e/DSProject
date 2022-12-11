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

for i in range(4):
    while not is_wall(): 
        step()
    while is_wall():
        right()
        paint()
