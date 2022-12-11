from pykkar import *

create_world("""
#########
#       #
#       #
#    >  #
#########
""")

n = 0
if get_direction() == "E":
    n = 3
elif get_direction() == "S":
    n = 2
elif get_direction() == "W":
    n = 1

while n > 0:
    right()
    n -= 1
    
nurk = 4
while nurk > 0:
    if is_wall() == False:
        step()
    else:
        right()
        right()
        right()
        if is_wall() == True:
            paint()
            nurk -= 1
        right()
        right()
        
    