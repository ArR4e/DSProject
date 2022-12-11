from pykkar import *

create_world("""
######
#    #
#    #
#    #
######
""")

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall ():
        break
    else:
        step()
        samme_jäänud -= 1

right()

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall ():
        break
    else:
        step()
        samme_jäänud -= 1

paint()
right()

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall ():
        break
    else:
        step()
        samme_jäänud -= 1

paint()
right ()

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall ():
        break
    else:
        step()
        samme_jäänud -= 1

paint()
right()

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall ():
        break
    else:
        step()
        samme_jäänud -= 1

paint()