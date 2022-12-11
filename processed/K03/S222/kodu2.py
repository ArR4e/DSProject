from pykkar import *

create_world("""
##########
#        #
#        #
#        #
#        #
#        #
#   >    #
#        #
##########
""")

def left():
    right()
    right()
    right()
    a = is_wall()
    right()
    return a

while is_painted() == False:
    if not is_wall():
        step()
    elif is_wall():
        if left():
            paint()
            right()
            step()
        else:
            right()
        
    
    