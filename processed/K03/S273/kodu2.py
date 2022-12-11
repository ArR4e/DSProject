from pykkar import *

create_world("""
#########
#       #
#       #
# <     #
#       #
#########
""")
while not is_wall():
    step()
right()
while not is_wall():
    step()
    if is_wall():
        paint()
        right()
    if is_painted():
        break
    
        
    