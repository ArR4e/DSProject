
from pykkar import *

create_world("""
##########
#        #
#        #
#   >    #
#        #
##########
""")
while not is_wall(): 
    step()
    if is_wall():
        right()
        right()
        right()
        break
i=4

while not is_wall() and 0<i: 
    step()
    if is_wall():
        right()
        paint()
        right()
        right()
        i=i-1
        

