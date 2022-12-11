from pykkar import *

create_world("""
########
#      #
#      #
#  >   #
#      #
#      #
########
""")

while not is_wall():
    step()
    
right()
i=4

while i>0:
    
    while not is_wall():
        step()

    paint()
    right()
    i-=1