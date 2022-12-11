from pykkar import *

create_world("""
##########
#        #
#E       #
#        #
#        #
#        #
##########
""")

while not is_wall(): 
    step()
    if is_wall():
        right()
    else:
        if is_wall():
            right()
            right()
        else: 
            if is_wall():
                right()
                right()
                right()
            else: 
                if is_wall():
                    right()
                    right()
                    right()
                    right()

    
?????? 