from pykkar import *

create_world("""
######
#    #
# >  #
#    #
#    #
######
""")
n = 0

while n < 5:
    while not is_wall():
        step()
    if n >= 1:
        paint()
        n += 1
    else:
        n += 1
    
    right()
    
