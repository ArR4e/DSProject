from pykkar import *
create_world("""
########
#      #
#      #
# v    #
#      #
#      #
########
""")
nurgad = 0
while not is_wall():
    step()
right()
while not nurgad == 4:
    if not is_wall():
        step()
    if is_wall():
        if not is_painted():
            paint()
            nurgad += 1
        right()
    
