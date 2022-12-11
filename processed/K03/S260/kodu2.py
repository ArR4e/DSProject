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

def sein():
    while not is_wall():
        step()
    right()
    move()

def move():
        paint()
        while not is_wall():
            step()
        if is_painted() == True:
            return    
        else:
            right()
            move()

sein()

