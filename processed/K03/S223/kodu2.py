from pykkar import *
 
create_world("""
#######
#     #
#   < #
#     #
#     #
#     #
#######
""")

def left():
    right()
    right()
    right()

def nurk():
    if is_wall():
        left()
        if is_wall():
            right()
            right()
            return True
        else:
            right()
        


nurgad = 0
while nurgad != 4:
    if nurk():
        paint()
        nurgad += 1
    else:
        if is_wall():
            right()
    step()
        
