from pykkar import *

create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")
samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall():
        paint()
        break
    else:
        step()
right()
while samme_jäänud > 0:
    if is_wall():
        paint()
        break
    else:
        step()
right()
while samme_jäänud > 0:
    if is_wall():
        paint()
        break
    else:
        step()
right()
while samme_jäänud > 0:
    if is_wall():
        paint()
        break
    else:
        step()
right()