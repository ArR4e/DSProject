#Pykkar igas maailma nurgas
from pykkar import*
create_world("""
#########
#       #
#       #
#       #
#       #
# <     #
#       #
#########
""")

värvitud = 0
while värvitud < 4:
    while not is_wall():
        step()
    if is_wall():
        right()
        if is_wall():
            right()
            right()
            paint()
            värvitud += 1
        else:
            right()
            right()