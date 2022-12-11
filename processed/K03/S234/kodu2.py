from pykkar import *
nurki=4
while nurki!=0:
    while is_wall()==False:
        step()
    right()
    while is_wall()==False:
        step()
    paint()
    right()
    nurki-=1