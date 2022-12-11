from pykkar import *

create_world("""
########
#^     #
#      #
#      #
#      #
#      #
########
""")

f = get_direction()
if f == "N":
    while not is_wall():
        step()
elif f == "W":
    right()
    while not is_wall():
        step()
elif f == "S":
    right()
    right()
    while not is_wall():
        step()
elif f == "E":
    right()
    right()
    right()
    while not is_wall():
        step()
    
d = False    
while d == False:
    right()
    while not is_wall():
        step()
    d = is_painted()
    paint()
