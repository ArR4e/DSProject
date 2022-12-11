from pykkar import *

create_world("""
#########
#      <#
#       #
#       #
#       #
#       #
#########
""")

#otsime nurga
while not is_wall():
    step()
right()
while not is_wall():
    step()
right()

#nurgad

while not is_painted():
    paint()
else:
    while not is_wall():
        step()
    right()
    
while not is_painted():
    paint()
else:
    while not is_wall():
        step()
    right()
    
while not is_painted():
    paint()
else:
    while not is_wall():
        step()
    right()
    
while not is_painted():
    paint()
else:
    while not is_wall():
        step()
    right()
    
#Ma proovisin välja mõelda, miks ta ei loopi korralikult aga ma ei tea..