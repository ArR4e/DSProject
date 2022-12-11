karp5=3
karp1=5
moos_kg=13

suuri_vaja=0
väikseid_vaja=0

def karpe_vaja(karp5,karp1,moos_kg):
    suuri_vaja=moos_kg//5
    väikseid_vaja=moos_kg-suuri_vaja*5
    print(suuri_vaja+väikseid_vaja)

karpe_vaja(karp5,karp1,moos_kg)       