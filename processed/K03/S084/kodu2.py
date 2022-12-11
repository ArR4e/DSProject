from pykkar import *

create_world("""
##########
#        #
#   >    #
#        #
#        #
#        #
#        #
#        #
##########
""")

#Robot läheb vastu seina
while not is_wall():
    step()
right()

while True:
    #Kui seina pole ees, siis liigub edasi
    while not is_wall():
        step()
    #Sein on ees, pöörab paremale
    right()
    #Kui all olev ruut on värvitud, lõpetab tegevuse. Kui pole, siis värvib selle
    if is_painted():
        break
    else:
        paint()