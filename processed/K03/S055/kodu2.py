from pykkar import *

create_world("""
########
#      #
#  >   #
#      #
#      #
#      #
########
""")

def otse():
    while not is_wall():
        step()

for i in range(5):
    otse()
    if i > 0:
        paint()
        print(i)
    right()

exit()
