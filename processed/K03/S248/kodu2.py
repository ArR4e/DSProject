from pykkar import *

create_world("""
########
#      #
#      #
#  >   #
#      #
########
""")

x=0

while x<5:
    if not is_wall():
        step()
    else:
        right()
        x=x+1
        if x>1:
            paint()
        continue

exitonclick()
    

        