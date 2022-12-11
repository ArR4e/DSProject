from pykkar import *
create_world("""
########
#      #
#      #
#   <  #
#      #
#      #
########
""")

while not is_wall(): # liigub seinani
    step()

right() # pöörab paremale

while not is_wall(): #liigub nurgani
    step()

if is_wall() and not is_painted(): #jõuab nurka ja kontrollib, kas on värvitud, kui ei, siis värvib
    paint()

right() # pöörab paremale
while not is_wall(): # liigub järgmise nurgani
    step()

if is_wall() and not is_painted():
    paint()

right()

while not is_wall():
    step()

if is_wall() and not is_painted():
    paint()

right()

while not is_wall():
    step()

if is_wall() and not is_painted():
    paint()

right()


exitonclick()
