from pykkar import *

create_world("""
##########
#        #
#        #
#    >   #
#        #
#        #
##########
""")

n=0
while is_wall()==False:
    step()

while n<4:
    right()
    while is_wall()==False:
        step()
    paint()
    n=n+1

