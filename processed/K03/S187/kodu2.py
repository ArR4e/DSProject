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

def seinani():
    while not is_wall():
        step()

varvitud = 0

seinani()
right()
seinani()
paint()
varvitud += 1

while is_wall() and is_painted() and varvitud < 5:
    right()
    seinani()
    paint()
    varvitud += 1
    
# palusin kaasõpilaselt abi ja sain lõpuks hakkama
# ei ole maha tehtud, aga arutasin natuke sõbraga ja sain lõpuks aru