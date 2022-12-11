import math

# Returns pole count
# Funktsioonid teevad koodi puhtamaks
def pole_count(road_len : int, max_dis : int):
    poles = road_len/max_dis
    return int(math.ceil(poles)) + 1

# Main loop
# Jällegi try/except block et välistada vigast sisendit kasutajalt
while True:
    try:
        road_len = int(input('Sisesta tee pikkus täisarvuna (meetrites): '))
        max_dis = int(input('Sisesta maksimaalne postide kaugus täisarvune (meetrites): '))
        print(pole_count(road_len, max_dis))
        break
    except:
        print('Palun sisesta väärtused täisarvudena!\n')

# Wait for input before closing
# Ootab userilt enterit enne kui kinni läheb.
# Automaatkontrollile ei meeldi
# input()