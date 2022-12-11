import pykkar
from pykkar import *
create_world("""
########
#      #
#      #
#      #
#      #
#      #
########
""")
while not is_wall():
    pykkar.step()
while is_wall():
    pykkar.right()
while not is_wall():
    pykkar.step()
while is_wall():
    pykkar.paint()
    pykkar.right()
while is_wall():
    pykkar.right()
while not is_wall():
    pykkar.step()
while is_wall():
    pykkar.paint()
    pykkar.right()
while is_wall():
    pykkar.right()
while not is_wall():
    pykkar.step()
while is_wall():
    pykkar.paint()
    pykkar.right()
while is_wall():
    pykkar.right()
while not is_wall():
    pykkar.step()
while is_wall():
    pykkar.paint()
    pykkar.right()
