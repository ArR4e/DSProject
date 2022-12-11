# https://courses.cs.ut.ee/2015/progmaa/spring/Main/Pykkar
from pykkar import *
create_world('''
###########
# >       #
#         #
###########
''')
while is_wall() == False:
    step()
a = False
right()
if is_wall == True:
    a = True
right()
if is_wall == True:
    a = True
right()
if is_wall == True:
    a = True
if a == False:
    while is_wall() == False:
        step()
for x in range (0, 4):
    paint()
    right()
    right()
    right()
    while is_wall() == False:
        step()