from pykkar import *

create_world("""
#########
#       #
#       #
#   <   #
#       #
#       #
#       #
#       #
#########
""")

while not is_wall():
    step()
      

else:
    paint()
    right()
    step()

  

#pykkar on väga kena loom, isegi ka ma teda nurkasid värvima ei saa..
    