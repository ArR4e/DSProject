from pykkar import *

create_world("""
#########
#       #
#       #
#    <  #
#       #
#       #
#########
""")
i = 0
while not is_wall() and i <= 4:
    i += 1
    step()
    if is_wall():
        right()
        u = 0
        while not is_wall() and u <= 4: 
            step()
            if is_wall():
                paint()
                right()
                u += 1
                
                
                
    