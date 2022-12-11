# 2. Pykkar igas maailma nurgas / RP

from pykkar import *

create_world("""
########
#      #
#   <  #
#      #
#      #
########
""")

painted = 0
walls = 0
while painted < 4:
    if not is_wall():
        step()
    else:
        right()
        if walls > 0:
            paint()
            painted += 1
        walls += 1
    
