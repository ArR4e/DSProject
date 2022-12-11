'''
Kirjuta Pykkari programm, mis suvalise ristkülikukujulise maailma puhul värvib ära maailma iga nurga.
Programm peab töötama olenemata roboti algpositsioonist ja vaatesuunast.
Võib eeldada, et maailm on seest tühi
(s.t pykkar asub ristkülikukujulises seest tühjas seintega piiratud maailmas).
'''

from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#      #
#      #
#  ^   #
#      #
#      #
########
""")
suund = get_direction()
# liigu seinani
while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
'''    
if suund == "E":
    print(suund)
if suund == "S":
    print(suund)
if suund == "W":
    print(suund)    
# pööra ringi
right()
right()
'''