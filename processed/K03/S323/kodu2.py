# kui pykkar sõidab kaks korda järjest vastu seina siis järelikult on ta nurgas

from pykkar import *

create_world("""
########
#      #
#      #
#      #
#  >   #
#      #
########
""")

while not is_wall():
    step()
right()

while not is_wall():
    step()
paint()
right()

while not is_wall():
    step()
paint()
right()

while not is_wall():
    step()
paint()
right()

while not is_wall():
    step()
paint()
right()