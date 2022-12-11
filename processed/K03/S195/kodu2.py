from pykkar import *

i = 0
p = 0

create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

while i < 4:
    if is_wall() and p > 0:
        if is_wall():
           paint()
           right()
           i = i + 1
        else:
            step()
        
    else:   
        if is_wall():
            right()
            p = 1
        else:
            step()

    
