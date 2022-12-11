from pykkar import *

create_world("""
#########
#       #
#       #
#  >    #
#       #
#       #
#########
""")

a=1
while True:
    if is_wall():
        if a == 1:
            a+=1
        else:
            paint()
        right()
    else:
        step()