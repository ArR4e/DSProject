from pykkar import *

create_world("""
########
#      #
#      #
#   <  #
#      #
#      #
########
""")
i=0
while i < 5:
    while not is_wall():
        step()
    while is_wall():
        if i==0:
            right()
            
        else:
            paint()
            right()
    i+=1
