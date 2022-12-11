suur = int(input("Mitu suurt karpi on Emmal? "))
väike = int(input("Mitu väikest karpi on Emmal? "))
kg = int (input("Mitu kilogrammi moos Emma keeab? "))
def moos(suur, väike, kg):
    maxsuured = int(kg/5)
    maxväiksed = kg - maxsuured*5
    if maxsuured <= suur:
        if maxväiksed <= väike:
            return (maxsuured + maxväiksed)
        else:
            return ("-1")
    else:
        return ("-1")
    return

moos(suur, väike, kg)