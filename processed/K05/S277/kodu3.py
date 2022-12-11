def moos(Ksuured, Kvaikesed, Kogumoos):
    Msuured = 5
    Mvaikesed = 1
    
    while Kogumoos == Msuured * Ksuured:
        return Ksuured
    while Kogumoos > Msuured * Ksuured:
        a = Kogumoos - Ksuured * Msuured
        if Kogumoos == Mvaikesed * Kvaikesed:
            return Ksuured + Kvaikesed
        else:
            return -1
  
print(moos(5, 1, 9))