from pykkar import *

create_world("""
########
#      #
#      #
#>     #
########
""")

while not is_wall():
    step()
right()
nurki_jäänud = 4
while nurki_jäänud>0:
    while not is_wall():
        step()
    paint()
    right()
    nurki_jäänud -=1
    
exitonclick()