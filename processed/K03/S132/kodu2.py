from pykkar import *

create_world("""
##########
#        #
#        #
#   v    #
#        #
#        #
##########
""")
def goto_wall():
    while not is_wall():
        step()
def paint_corners():
    goto_wall()
    right()
    goto_wall()
    paint()
    right()
    goto_wall()
    paint()
    right()
    goto_wall()
    paint()
    right()
    goto_wall()
    paint()
    
paint_corners()
