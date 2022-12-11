from pykkar import *

create_world("""
############
#          #
#          #
#      <   #
#          #
############
""")

corner_count = 0
while corner_count != 4:
    if is_wall():
        for i in range(2):
            right()
            if is_wall():
                paint()
                corner_count += 1
                break
        right()
    else:
        step()
        