from pykkar import *

create_world("""
#########
#       #
#       #
#       #
#       #
#      <#
#########
""")

while not is_wall():
    step()
else:
    right()

if not is_wall():
    right()
else:
    paint()

if not is_wall():
    right()
else:
    paint()
    
while is_painted():
    step()
  
while not is_wall():
    step()
else:
    right()
    right()
    right()

paint()

while not is_wall():
    step()
else:
    right()
    right()
    right()

paint()

while not is_wall():
    step()
else:
    right()
    right()
    right()

paint()

while not is_wall():
    step()
else:
    right()
    right()
    right()

paint()