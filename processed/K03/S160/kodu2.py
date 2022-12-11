from pykkar import *

create_world("""
########
#      #
#      #
#      #
#   >  #
#      #
########
""")

punkt = 0

while punkt <= 5:
    
    if not is_wall():
        step()
        
    elif is_wall:
        right()
        punkt += 1
        
        if 1 < punkt < 6:
            paint()