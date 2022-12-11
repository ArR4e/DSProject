from pykkar import *

create_world("""
########
#      #
#      #
#      #
#  v   #
#      #
########
""")


if not is_wall():
    step()
    while not is_wall():
        step()
if is_wall():
    right()
    while not is_wall():
        step()
        if is_wall():
            right()
            paint()
if is_wall():
    right()
    while not is_wall():
        step()
        if is_wall():
            right()
            paint()
        
    
        
            

            

