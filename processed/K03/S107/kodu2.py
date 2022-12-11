from pykkar import *

create_world('''
##########
#        #
#        #
#        #
#      < #
#        #
##########
''')
#Kui seina pole, siis robot kõnnib.
while not is_wall():
        step()
        
#Kui sein ees, siis robot pöörab seni paremale kuni seina
#pole ja värvib järgmise seinavastus oleva põranda tumedaks ning jätkab oma tegevust.
while True:

    if is_wall():
        right()
        
    else:
        step()


    if is_wall():
            right()
            paint()
