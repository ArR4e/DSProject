from pykkar import *

create_world("""
##################
#                #
#                #
#                #
#         <      #
#                #
#                #
#                #
##################
""")

samme = 10000

while  samme > 0:
    if is_wall():
        break
    else:
        step()
        samme -= 1
right()

while samme > 0:
    if is_wall():
        break
    else:
        step()
        samme -=1
paint()
right()
while samme > 0:
    if is_wall():
        break
    else:
        step()
        samme -=1
paint()
right()

while samme > 0:
    if is_wall():
        break
    else:
        step()
        samme -=1
paint()
right()

while samme > 0:
    if is_wall():
        break
    else:
        step()
        samme -=1
paint()
right()
        
