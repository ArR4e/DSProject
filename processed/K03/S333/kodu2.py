from pykkar import *

create_world("""
########
#<     #
#      #
#      #
#      #
#      #
########
""")



n= 0
i= 1

while n< 4:
    while is_wall():
        right()
#kontrollib, ega nina vastu seina pole
    while i== 1:
        step()
        if is_wall():
            right()
            i+= 1
#alge tsükkel, et jõuda mõne seinani ja pöörata paremale
    while i== 2 and n<4 :
        if not is_wall():
            step()
#juhul kui seina ees pole, kõnni kuni leiad seina
        elif is_wall():
            paint()
            right()
            n+= 1
#juhul kui leiad seina uuesti, värvi nurk ja liigu edasi
#loendab nurkasid, et neljandas nurgas programm seisma jääb.