from pykkar import *

create_world("""
########
#      #
#   <  #
#      #
#      #
#      #
########
""")
varvitud = 0
while varvitud<=4:
    if is_wall():
        right()
        if is_wall():
            paint()
            varvitud +=1
            right()
        else:
            right()
            right()
    else:
        step()

